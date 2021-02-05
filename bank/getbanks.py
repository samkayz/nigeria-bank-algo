class GetBank:

    def GetLikeBank(self, accountNumber):
        Banks = [
            { 'name': "ACCESS BANK", 'code': "044" },
            { 'name': "CITIBANK", 'code': "023" },
            { 'name': "DIAMOND BANK", 'code': "063" },
            { 'name': "ECOBANK NIGERIA", 'code': "050" },
            { 'name': "FIDELITY BANK", 'code': "070" },
            { 'name': "FIRST BANK OF NIGERIA", 'code': "011" },
            { 'name': "FIRST CITY MONUMENT BANK", 'code': "214" },
            { 'name': "GUARANTY TRUST BANK", 'code': "058" },
            { 'name': "HERITAGE BANK", 'code': "030" },
            { 'name': "JAIZ BANK", 'code': "301" },
            { 'name': "KEYSTONE BANK", 'code': "082" },
            { 'name': "PROVIDUS BANK", 'code': "101" },
            { 'name': "SKYE BANK", 'code': "076" },
            { 'name': "STANBIC IBTC BANK", 'code': "221" },
            { 'name': "STANDARD CHARTERED BANK", 'code': "068" },
            { 'name': "STERLING BANK", 'code': "232" },
            { 'name': "SUNTRUST", 'code': "100" },
            { 'name': "UNION BANK OF NIGERIA", 'code': "032" },
            { 'name': "UNITED BANK FOR AFRICA", 'code': "033" },
            { 'name': "UNITY BANK", 'code': "215" },
            { 'name': "WEMA BANK", 'code': "035" },
            { 'name': "ZENITH BANK", 'code': "057" }
        ]

        algo = [3, 7, 3, 3, 7, 3, 3, 7, 3, 3, 7, 3]

        # acct = '0020657879'


        account_list = list(accountNumber)
        interger_of_account = list(map(int, account_list))
        # print(interger_of_account[0:9])

        codelist = []
        for data in Banks:
            j = list(data['code'])
            codelist.append(j)
    
        # print(codelist)
        dataset = []
        for i in codelist:
            datas = {}
            d = list(i)
            d = list(map(int, d))
            all_list = (d + interger_of_account[0:9])
            checksum = interger_of_account[-1]
            # print(all_list)
            total = 0
            ele = 0
            res_list = [algo[i] * all_list[i] for i in range(len(algo))]
            while(ele < len(res_list)):
                total = total + res_list[ele]
                ele += 1
     
            # printing total value
            # print(type(total))
            mod = total % 10
            # print(mod)
            check = 10 - mod
            # print(check)
            code = all_list[0:3]
            if check == checksum or check == 10:
                i[0:3] = [''.join(i[0:3])]
                datas['code'] = i[0]
                dataset.append(datas)
            # print(f'{i[0]}-{check}')
        # print(dataset)


        final_result = []
        for codes in dataset:
            valueData = {}
            for i in Banks:
                if i['code'] != codes['code']:continue
                valueData['code'] = i['code']
                valueData['name'] = i['name']
                final_result.append(valueData)


        # print(final_result)
        return final_result