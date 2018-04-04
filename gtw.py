import time
import os
from steem import Steem
from steem.account import Account
from steem.amount import Amount
from steem.transactionbuilder import TransactionBuilder
from steembase import operations


def get_witness(block_num,block_witness,s):
		witness = s.get_block_header(block_num)['witness']
		block_witness[block_num]=witness
		
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime()),flush=True) 

nodes = ['https://api.steemit.com']
s = Steem(nodes=nodes)
username='gtw'
try:
	maccount = Account(username,s)
except Exception as e:
	print(e)
	exit()

password="your_password_to_unlock_your_wallet"
os.environ["UNLOCK"] = password
user = username
block_file="gtw_blocks.txt"
lb=1
with open(block_file, 'r') as f:
	for line in f.readlines():
		lb = int(line)

mlb = lb
ac = Account(user,s)
block_witness={}
transfers = []
hrl = ac.history_reverse(filter_by='transfer',raw_output=False)

for op in hrl:
	if op['block'] <= lb:
		break
	block_num = op['block']
	if op['block'] > mlb:
		mlb = op['block']
		with open(block_file, 'a+') as f:
			f.write("%s\n" % str(mlb))
	am = Amount(op['amount'])
	if am.amount==0.002 and am.asset=='SBD' and op['to']==username:
		if block_num not in block_witness:
			get_witness(block_num,block_witness,s)
		guess = op['memo'].strip('@')
		if guess == block_witness[block_num]:
			memo = 'Your guess was right! Witness for block '+str(block_num)+' was '+guess
			trx = {'memo':memo,'from':username,'to':op['from'],'amount':'0.021 SBD'}
			
		else:
			memo = 'Sorry, but for block '+str(block_num)+' the witness was '+block_witness[block_num]+' and not '+guess+' as you guessed. Try again!:)'
			trx = {'memo':memo,'from':username,'to':op['from'],'amount':'0.001 SBD'}
		transfers.append(trx)
if transfers:
	tb = TransactionBuilder()
	operations = [operations.Transfer(**x) for x in transfers]
	tb.appendOps(operations)
	tb.appendSigner(username, 'active')
	tb.sign()
	tx = tb.broadcast()
	print(tx)