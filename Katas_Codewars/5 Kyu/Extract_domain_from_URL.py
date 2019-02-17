# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 
# For example:
# 	domain_name("http://github.com/carbonfive/raygun") == "github" 
# 	domain_name("http://www.zombie-bites.com") == "zombie-bites"
# 	domain_name("https://www.cnet.com") == "cnet"


def domain_name(url):
    if url.index(".") < 12:
        url = url.split(".")
        return url[1]
    else:
        start_link = url.find('/')
        start_quote = url.find('/', start_link + 1)
        end_quote = url.find('.', start_quote + 1)
        url = url[start_quote + 1: end_quote]
        return url


## Better use of split
##	1st divide http:// y github.com/carbonfive/raygun , nos quedamos con el segundo
##	2nd divide github.com  /  carbonfive  /  raygun , nos quedamos el primero, que corresponde al dominio y no sus subapartados
##	3rd divide www . cnet . com,  elimina el dominio y coje el siguiente segmento, al contar desde el final no tiene en cuenta el www.

def domain_name2(url):
  url = url.split('//')[-1]
  url = url.split('/')[0]
  url = url.split('.')[-2]
  return url



if __name__ == '__main__':
	
## Test 1
	assert domain_name("http://github.com/carbonfive/raygun") == "github" 
	assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
	assert domain_name("https://www.cnet.com") == "cnet"

## Test 
	assert domain_name2("http://github.com/carbonfive/raygun") == "github" 
	assert domain_name2("http://www.zombie-bites.com") == "zombie-bites"
	assert domain_name2("https://www.cnet.com") == "cnet"

