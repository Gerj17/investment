from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as Soup
from pathlib import Path
from Invest.core.WebAccess import parse_website
import time

save_location = Path(Path.home(), "Desktop")


# urls = {"EC-Share Index": "http://www.ecseonline.com/ecse_index.php", }
# url = "http://www.ecseonline.com/ecse_index.php"

"""def parse_website(website):
    client = urlopen(website)
    client_read = client.read()
    client.close()
    client_soup = Soup(client_read, "html.parser")
    return client_soup"""


def EC_Share_Index(web_page="http://www.ecseonline.com/ecse_index.php"):
    """
    Writes the market value of the index in a Csv file.
    :param web_page: the Easter Caribbean index webpage.
    :return: None
    """
    page = parse_website(web_page)

    # -----Get info from webpage-----
    info_table = page.findAll("table", {"width": "50%"}).pop()
    security_name = info_table.tbody.tr.td.p.text
    print("Name of Security ---> ", security_name)
    current_date = info_table.findAll("td")[1].text[2:]
    market_value = info_table.findAll("td")[2].text

    #  -----
    filename = security_name + ".csv"
    file = Path(save_location, filename)
    print("Location of Flile ---> ", file)

    if file.is_file():
        print("T/F Does the file already exist? ---> ", 'True')
        #  Check last date with current date to ensure no duplicates
        with open(file, "r") as f:
            a = f.read().replace("\n", ":")
            content = a.strip().split(":")
            last_entry = content[len(content) - 2:len(content) - 1]
            string = ''.join(last_entry)
            last_date = string[:len(string) - 7].strip()

            #  print("last_date",last_date)
            #  print("Date", date)
            if last_date.strip() == current_date.strip():
                # print("\n", "An entry for", current_date.strip(), "was already made")
                print("\n", "An entry for", last_date.strip(), "was already made")
                time.sleep(5)
                return

        doc = open(file, "a")
        doc.write(current_date + "," + market_value + "\n")
    else:
        print("false")
        doc = open(file, "a")
        title = "Security Name: " + str(security_name) + "\n"
        headers = "Date, Market Value\n"

        doc.write(title)
        doc.write(headers)
        doc.write(current_date + "," + market_value + "\n")

    doc.close()
    print("\n", "A New Entry for", current_date.strip(), "Made ")
    time.sleep(9)
    return


EC_Share_Index()
