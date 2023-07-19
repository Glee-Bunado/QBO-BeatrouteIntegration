invoice = {

    'AllowIPNPayment': False,
    'AllowOnlinePayment': False,
    'AllowOnlineCreditCardPayment': False,
    'AllowOnlineACHPayment': False,
    'domain': 'QBO',
    'sparse': False,
    'Id': '103',
    'SyncToken': '1',
    'MetaData': {
        'CreateTime': '2023-06-20T13:41:59-07:00',
        'LastModifiedByRef': {'value': '9130357082944686'},
        'LastUpdatedTime': '2023-06-20T13:42:08-07:00'
    },
    'CustomField': [
        {
            'DefinitionId': '1',
            'Name': 'Crew #',
            'Type': 'StringType'
        }
    ],
    'DocNumber': '1033',
    'TxnDate': '2023-06-20',
    'CurrencyRef': {
        'value': 'USD',
        'name': 'United States Dollar'
    },
    'LinkedTxn': [
        {
            'TxnId': '41',
            'TxnType': 'Estimate'
        }
    ],
    'Line': [
        {
            'Id': '1',
            'LineNum': 1,
            'Description': 'Rock Fountain',
            'Amount': 275.0,
            'LinkedTxn': [
                {
                    'TxnId': '41',
                    'TxnType': 'Estimate'
                }
            ],
            'DetailType': 'SalesItemLineDetail',
            'SalesItemLineDetail': {
                'ItemRef': {
                    'value': '5',
                    'name': 'Rock Fountain'
                },
                'UnitPrice': 275,
                'Qty': 1,
                'ItemAccountRef': {
                    'value': '48',
                    'name': 'Landscaping Services:Job Materials:Fountains and Garden Lighting'
                },
                'TaxCodeRef': {
                    'value': 'TAX'
                }
            }
        },
        {
            'Id': '2',
            'LineNum': 2,
            'Description': 'Custom Design',
            'Amount': 262.5,
            'LinkedTxn': [
                {
                    'TxnId': '41',
                    'TxnType': 'Estimate'
                }
            ],
            'DetailType': 'SalesItemLineDetail',
            'SalesItemLineDetail': {
                'ItemRef': {
                    'value': '4',
                    'name': 'Design'
                },
                'UnitPrice': 75,
                'Qty': 3.5,
                'ItemAccountRef': {
                    'value': '82',
                    'name': 'Design income'
                },
                'TaxCodeRef': {
                    'value': 'NON'
                }
            }
        },
        {
            'Id': '3',
            'LineNum': 3,
            'Description': 'Fountain Pump',
            'Amount': 45.0,
            'LinkedTxn': [
                {
                    'TxnId': '41',
                    'TxnType': 'Estimate'
                }
            ],
            'DetailType': 'SalesItemLineDetail',
            'SalesItemLineDetail': {
                'ItemRef': {
                    'value': '11',
                    'name': 'Pump'
                },
                'UnitPrice': 22.5,
                'Qty': 2,
                'ItemAccountRef': {
                    'value': '48',
                    'name': 'Landscaping Services:Job Materials:Fountains and Garden Lighting'
                },
                'TaxCodeRef': {
                    'value': 'TAX'
                }
            }
        },
        {
            'Amount': 582.5,
            'DetailType': 'SubTotalLineDetail',
            'SubTotalLineDetail': {}
        }
    ],
    'TxnTaxDetail': {
        'TxnTaxCodeRef': {
            'value': '2'
        },
        'TotalTax': 46.6,
        'TaxLine': [
            {
                'Amount': 46.6,
                'DetailType': 'TaxLineDetail',
                'TaxLineDetail': {
                    'TaxRateRef': {
                        'value': '3'
                    },
                    'PercentBased': True,
                    'TaxPercent': 8,
                    'NetAmountTaxable': 582.5
                }
            }
        ]
    },
    'CustomerRef': {
        'value': '10',
        'name': 'Geeta Kalapatapu'
    },
    'CustomerMemo': {
        'value': 'Thank you for your business and have a great day!'
    },
    'BillAddr': {
        'Id': '87',
        'Line1': 'Geeta Kalapatapu',
        'Line2': '1987 Main St.',
        'Line3': 'Middlefield, CA  94303',
        'Lat': '37.4530553',
        'Long': '-122.1178261'
    },
    'ShipAddr': {
        'Id': '10',
        'Line1': '1987 Main St.',
        'City': 'Middlefield',
        'CountrySubDivisionCode': 'CA',
        'PostalCode': '94303',
        'Lat': '37.445013',
        'Long': '-122.1391443'
    },
    'FreeFormAddress': True,
    'SalesTermRef': {
        'value': '3',
        'name': 'Net 30'
    },
    'DueDate': '2023-07-20',
    'TotalAmt': 629.1,
    'ApplyTaxAfterDiscount': False,
    'PrintStatus': 'NeedToPrint',
    'EmailStatus': 'NotSet',
    'BillEmail': {
        'Address': 'Geeta@Kalapatapu.com'
    },
    'Balance': 629.1
}
