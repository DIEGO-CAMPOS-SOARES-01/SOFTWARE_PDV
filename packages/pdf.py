import pdfkit
import pandas as pd
import webbrowser


config = pdfkit.configuration(wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
def gen_os(df,total):
    table = df.to_html()
    pdf = ("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <style>  
        .header{
            text-align:left;
            font: 9px Calibri;
            line-height:0.6;
            margin-left: 5em; 
            margin-top:15em;
        }
        .info{
            text-align:left;
            font: 9px Calibri;
            line-height:1px;
            margin-left: 5em;
        }
        .table{
            margin-top:10px;
            text-align:center;
            font: 12px Calibri; 
        }
        table,tr{
            border-collapse:collapse;
            margin-left:auto;
            margin-right:auto;
            text-align:center;
            font: 16px Calibri;    
        }
        th{ 
            font: 16px Calibri;
            background:#000;
            color:white;
            text-align:center;
            padding:6px 
            }

        tr:nth-child(even){background-color:#eeeeee;}
    </style>    
    <body>
        <div class = "header">
            <h1>Nome Da Loja</h1>
            <h1>Endereço</h1>
            <h1>Tel: (21)99999-9999</h1>
            <h1>Email :email@gmail.com</h1>
            <hr>
        </div>
        <div class = "info">
            <h1>Cliente: </h1><hr>
            <h1>Endereço</h1><hr>
            <h1>Cidade</h1><hr>
            <h1>Tel: </h1><hr>
            
        </div>
        <div class = "table">
            <h1>Descriçao Do Pedido</h1>
            %s
            <h1>Total : %s </h1>
        </div>

    </body>
    </html>""" %(table,total))

    pdfkit.from_string(pdf, output_path= "PDF.pdf",configuration= config)
    url = 'PDF.pdf'

    webbrowser.open(url,new=1)




