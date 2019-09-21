from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as Soup
from pathlib import Path
from Invest.core.WebAccess import parse_website
import time
import  sys

save_location = Path(Path.home(), "Desktop","EC  index")


# urls = {"EC-Share Index": "http://www.ecseonline.com/ecse_index.php", }
# url = "http://www.ecseonline.com/ecse_index.php"


def EC_Share_Index(web_page="http://www.ecseonline.com/ecse_index.php"):
    """
    Writes the market value of the index in a Csv file.
    :param web_page: the Easter Caribbean index webpage.
    :return: None
    """

    def end_message(market_value):
        """
        :market_value: last available point status of the market
        """
        print( f" \n {market_value} Points \n ")
        print("\n  thanks for the time byee :P : \n")
        time.sleep(10)



    page = parse_website(web_page)

    # -----Get info from webpage-----
    info_table = page.findAll("table", {"width": "50%"}).pop()
    security_name = info_table.tbody.tr.td.p.text
    print("Name of Security ---> ", security_name)
    current_date = info_table.findAll("td")[1].text[2:]
    market_value = info_table.findAll("td")[2].text

    #  -----File Name and Path-------
    filename = security_name + ".csv"
    file = Path(save_location, filename)
    print("Location of File ---> ", file)

    if file.is_file():
        print("T/F Does the file already exist? ---> ", 'True')

        #  Check last date with current date to ensure no duplicates
        with open(file, "r") as f:
            a = f.read().replace("\n", ":")
            content = a.strip().split(":")
            last_entry = content[len(content) - 2:len(content) - 1]
            string = ''.join(last_entry)
            last_date = string[:len(string) - 7].strip()

            if last_date.strip() == current_date.strip():
                print(f"\n An entry for {last_date.strip()} was already made  :P :) ")
                end_message(market_value)
                return

        doc = open(file, "a")
        #  write data for current date 
        doc.write(current_date + "," + market_value + "\n")
    else:
        #create a new file if there is no existing file
        print(f"false \n now creating a new file {None} ")
        doc = open(file, "a")
        title = "Security Name: " + str(security_name) + "\n"
        headers = "Date, Market Value\n"

        doc.write(title)
        doc.write(headers)
        doc.write(current_date + "," + market_value + "\n")
        end_message(market_value)



    doc.close()
    print("\n", "A New Entry for", current_date.strip(), "Was Made :P :) ")
    end_message(market_value)
    return


