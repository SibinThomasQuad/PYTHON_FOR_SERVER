from selenium import webdriver
from urllib.parse import urlparse
import requests

DOMAIN_LIST_FILE = "domains.txt"
OUTPUT_FILE_PREFIX = "SCREEN_"

class Output:
    def show(self,response,screen_shot):
        return "[+] Status : "+str(response.status_code)+"Screen Shot : "+str(screen_shot)

class Domain:
    def __init__(self) -> None:
        test_obj = Image()
        network = Network()
        output = Output()
        self.network = network
        self.test_obj = test_obj
        self.output = output
        pass
    
    def itrate(self):
        with open(DOMAIN_LIST_FILE, 'r') as file:
            for url in file:
                domain_name = self.get_domain_name(url)
                out_put_file = OUTPUT_FILE_PREFIX+str(domain_name)+".png"
                web_respose = self.network.web_response(url)
                self.test_obj.capture_screenshot(url,out_put_file)
                print(self.output.show(web_respose,out_put_file))
    
    def get_domain_name(self,url):
        parsed_url = urlparse(url)
        domain_name = parsed_url.netloc
        return domain_name

class Network:
    def web_response(self,url):
        response = requests.get(url,verify=False)
        return response
        
class Image:
    def capture_screenshot(self,url,output_file):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

        try:
            driver.get(url)
            driver.save_screenshot(output_file)
            print("Screenshot captured successfully!")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            driver.quit()

class Main:
    def __init__(self) -> None:
        domain = Domain()
        self.domain = domain
        pass
    def start_test(self):
        self.domain.itrate()

main = Main()
main.start_test()


