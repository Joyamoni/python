

def check_mail_existance(email):
	import smtplib
	from email.message import EmailMessage
	import dns.resolver

	global exists_bool
	global accept_all_bool

	email_from="python@finderbd.com"

	domain=email.replace("@"," ").split()[-1]

	local_host=smtplib.SMTP()
	#local_host.set_debuglevel(2)

	message = EmailMessage()
	message["Subject"]="hello from python"
	message["To"]=email
	message["From"]=email_from
	message["Body"]="dear hi we are so pleased to meet you"

	mail_servers=dns.resolver.resolve(domain,"MX")	
	li=[]
	for each_server in mail_servers:
		li.append(str(each_server))
	first_server=li[0].split()[-1]


	try:
		local_host.connect(first_server)
		local_host.send_message(message)
		exists_bool=True
		
	except Exception as each_exception:
		"""each_exception=str(each_exception)
								each_exception=eval(each_exception)
								message=each_exception[email]
								code=(str(message).split()[0])[1:-1]
								print(code)"""
		exists_bool=False
		
	return exists_bool
			


def accept_all_check(email):
	domain=email.replace("@"," ").split()[-1]
	abol_tabol_email=f"abol_tabol_email_@{domain}"

	accept_all_bool=check_mail_existance(abol_tabol_email)
	return(accept_all_bool)




