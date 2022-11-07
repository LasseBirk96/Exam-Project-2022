from Security.InputSanitizer import InputSanitizer

sani = InputSanitizer()

data = {
	"email":"test@gmail.com",
	"account_number":"123456789012",
	"CVV":"012",
	"pin_code":"2222222",
	"balance":500
}


print(sani.__clean_CVV("123121"))


sani.clean_input(data)








