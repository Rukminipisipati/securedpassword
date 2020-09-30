import requests
import hashlib
import sys
def request_api_data(query_char):
	url='https://api.pwnedpasswords.com/range/'+ query_char
	res=requests.get(url)
	if res.status_code!=200:
		raise RunTimeError(f'Error fetching: {res.status_code},please try again')
	return res
def get_password_leaks_count(hashes,hash_to_check):
	#print(response.text) # all hashes that has the first_5 matching with the count of each hash
	hashes=(line.split(':') for line in hashes.text.splitlines())
	for h,count in hashes:
		if h==hash_to_check:
			return count
	return 0
		
def pwned_api_check(password):
	passw=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first_5,tail=passw[:5],passw[5:]
	response=request_api_data(first_5)
	#print(response)
	return get_password_leaks_count(response,tail)
def main(args):
	for password in args:
		count=pwned_api_check(password)
		if count:
			print(f'{password} exists for {count} times. You probably need to change it')
		else:
			print(f'{password} was not found. carry on!')
	return 'done!'


if __name__=='__main__':
	sys.exit(main(sys.argv[1:]))
	

