__author__ = "DreMan360"
__version__ = '08-02-2022' #thought an update date would be better


import shodan
import json
import nextcord     
from nextcord.ext import commands
from random import randint
import asyncio



intents = nextcord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
intents.members = True

ApiKey = '' # Add your shodan API key
botToken = '' # Add your discord bot token


api = shodan.Shodan(ApiKey)



def get_data():
    with open("sample.json","r") as f:
        users = json.load(f)

    return users


def get_count_data():
    with open("ranIpcount.json","r") as f:
        users = json.load(f)

    return users

def get_ip_data():
    with open("ipList.json","r") as f:
        users = json.load(f)

    return users


#Get a random IP with random version
@client.command()
async def ranip(ctx):
    users = get_data()
    counter = get_count_data()
    allips = get_ip_data()

    print('running')

    if counter["Count"] <= 99: # Check if the counter should reset

        theList = list((users["matches"][int(counter["Count"])]).values())

        if theList[-1] != [] and '.' in theList[-1] and '.' in theList[12]: # The IP and version could be different, so check
            print('Solution 1')

            ipemb = nextcord.Embed(title="a random minecraft server", color=nextcord.Color.blurple())
            ipemb.add_field(name='IP Address',value=str(theList[-1]))
            ipemb.add_field(name='Version',value=str(theList[12]))


            counter["Count"] += 1


            await ctx.reply(embed=ipemb)

            with open("ranIpcount.json", "w") as f:
                json.dump(counter,f, indent=4)
            return True


        elif theList[14] != [] and '.' in str(theList[14]) and '.' in str(theList[2]): 
            print('Solution 2')

            ipemb = nextcord.Embed(title="a random minecraft server", color=nextcord.Color.blurple())
            ipemb.add_field(name='IP Address',value=str(theList[14]))
            ipemb.add_field(name='Version',value=str(theList[2]))


            await ctx.reply(embed=ipemb)

            counter["Count"] += 1

            with open("ranIpcount.json", "w") as f:
                json.dump(counter,f, indent=4)
            return True

        elif theList[15] != [] and '.' in theList[15] and '.' in theList[11]:
            print('Solution 3')


            ipemb = nextcord.Embed(title="a random minecraft server", color=nextcord.Color.blurple())
            ipemb.add_field(name='IP Address',value=str(theList[15]))
            ipemb.add_field(name='Version',value=str(theList[11]))


            counter["Count"] += 1


            await ctx.reply(embed=ipemb)

            with open("ranIpcount.json", "w") as f:
                json.dump(counter,f, indent=4)
            return True


        else:
            await ctx.reply('error: rerun command')
            counter["Count"] += 1
            print(theList[-1])
            print(theList[12])

            with open("ranIpcount.json", "w") as f:
                json.dump(counter,f, indent=4)
            return True
    
    elif counter["Count"]==100: # Reset Counter

        print("aaaa")

        counter["Count"] = 0

        await ctx.reply('error: rerun command')



        out_file = open("sample.json", "w")
        
        json.dump(api.search('minecraft'), out_file, indent = 4)
        
        out_file.close()

        with open("ranIpcount.json", "w") as f:
            json.dump(counter,f, indent=4)
        return True




# Get a completely new IP list
@client.command()
async def forcereset(ctx):
    out_file = open("sample.json", "w")
    json.dump(api.search('minecraft'), out_file, indent = 4)
    
    out_file.close()


    await ctx.reply("success!")



# Get an IP with a specific version
@client.command()
async def filterip(ctx, inputversion):
    users = get_data()
    allips = get_ip_data()



    print('running')

    versionList = ["1.19","1.19.1","1.19.2","1.18.2","1.18.1","1.12.2"] # Feel free to add more versions

    if inputversion not in versionList:
        await ctx.reply("Not a valid version, please input one of the following: "+str(versionList))
    
    elif inputversion in versionList:


        for i in range(100):

            print(i)

            theList = list((users["matches"][i]).values())

            if theList[-1] != [] and '.' in str(theList[-1]) and '1' in str(theList[12]) and theList[-1] != None and theList[12] != None and "[" not in str(theList[12]):
                print('Solution 1')

                ip = theList[-1]
                version = theList[12]


                

            


            elif theList[14] != [] and '.' in str(theList[14]) and '.' in str(theList[2]):
                print('Solution 2')

                ip = theList[14]
                version = theList[2]



            elif theList[6] != [] and '.' in theList[6] and '.' in str(theList[2]) and theList[6] != None and theList[6] != None:
                print('Solution 4')

                ip = theList[6]
                version = theList[2]




            else:
                ip = 0
                version = 0

            

            if version == str(inputversion):


                if ip in allips.keys():
                    pass
                else:
                    await ctx.reply(ip)

                    out_file = open("sample.json", "w")
                    json.dump(api.search('minecraft'), out_file, indent = 4)
                    
                    out_file.close()

                    allips[ip] = 0

                    break

            else:
                pass

        with open("ipList.json", "w") as f:
            json.dump(allips,f, indent=4)
        return True





# Get a list of (up to) 40 IPs
@client.command()
async def multip(ctx, amount):
    users = get_data()
    counter = get_count_data()    
    ip = 0
    version = 0
    theMax = 40 # Feel free to increase

    ipemb = nextcord.Embed(title="your list, lord person", color=nextcord.Color.blurple())

    if int(amount) > theMax: 
        await ctx.reply("Max is "+str(theMax))

    else:


        for i in range(int(amount)):
            theList = list((users["matches"][i]).values())

            if theList[-1] != [] and '.' in str(theList[-1]) and '1' in str(theList[12]) and theList[-1] != None and theList[12] != None and "[" not in str(theList[12]):
                print('Solution 1')

                ip = theList[-1]
                version = theList[12]


                

            


            elif theList[14] != [] and '.' in str(theList[14]) and '.' in str(theList[2]):
                print('Solution 2')

                ip = theList[14]
                version = theList[2]


                

            elif theList[6] != [] and '.' in theList[6] and '.' in str(theList[2]) and theList[6] != None and theList[6] != None:
                print('Solution 4')

                ip = theList[6]
                version = theList[2]


            else:
                ip = "ERROR"
                version = "ERROR"



            ipemb.add_field(name=f"IP: {ip} - Version: {version}",value="\u200b")

        await ctx.reply(embed=ipemb)



        out_file = open("sample.json", "w")
        json.dump(api.search('minecraft'), out_file, indent = 4)
        
        out_file.close()





client.run(botToken)








