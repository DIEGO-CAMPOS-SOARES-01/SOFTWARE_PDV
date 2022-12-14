import pdfkit
import pandas as pd
import webbrowser
import os

if os.name == 'nt':
    config = pdfkit.configuration(wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
else:
    config = pdfkit.configuration(wkhtmltopdf = r"/usr/local/bin/wkhtmltopdf")
def gen_os(df,info):
    table = df.to_html()
    pdf = (f"""
      <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  </head>
  <style>
      body{{
          font: 10pt Times New Roman;
          line-height:4pt;
          text-align:center;
          margin:10px 10px 0 
      }}
      .table table,tr{{
          border-collapse:collapse;
          margin: 20px 0 20px 0; 
          line-height:18pt;
          width:100%;
      }}
      .table th{{
          background:#000;
          color:white;
          text-align:center;
          padding:6px 
      }}
      .table tr:nth-child(even){{
          background-color:#eeeeee;
      }}
  </style>    
  <body>
      <div style="border: 1px solid black;font-size: 8pt;">
          <h1 style="font-size: 18pt;">JC VIDROS</h1>
          <h2></h2>
          <h2>Rua Visconde De Itauna 1638</h2>
          <h2>Gradim - São Gonçalo - RJ - Cep: 24431182</h2>
          <h2>Tel: (21) 96968-4788</h2>
          <h2>E-mail : carlosaugusto280475@gmail.com</h2>

      </div>
      
      <table style="border:1px solid black;border-collapse:collapse;width:100%;">
          <tbody>
              <tr style="height:19pt;">
                  <td style="width:200pt">Emitido Em: {info["emiçao"]} </td>
                  <td style="width:200pt">Valido Ate: {info["delivery"]}</td>
              </tr>
          </tbody>
          </table>
      
      <div>
        <table style="text-align: center;height:15pt;border: 1px solid black; width:100%;margin-top:10px;">
            <tbody>
                <tr >
                    <td>CLIENTE</td>
                </tr>
            </tbody>
        </table>
      <table style="border:1px solid black;border-collapse:collapse;width:100%;">
          <tbody style="text-align: left;height: 60pt;">
              <tr  style = "border: 1px solid black">
                  <td style="width: 10pt;">Cliente: {info["Nome"]} </td>
                  <td></td>
              </tr>
              <tr>
                  <td style="width: 10pt;">Tel(1): {info["Tel1"]}</td>
                  <td style="width: 10pt;"> Tel(2): {info["Tel2"]}</td>
              </tr>
              <tr style="border: 1px solid black;height:19pt;">
                  <td>CPF/CNPJ:{info["cpf"]}</td>
                  <td>Email:{info["email"]}</td>
              </tr>
              <tr >
                  <td >Endereço: {info["end"]} </td>
                  <td></td>
              </tr>
              <tr style="border: 1px solid black;height:19pt;">
                  <td>Bairro:{info["brr"]}</td>
                  <td>Cidade:{info["cdd"]}</td>
              </tr>
          </tbody>
      </table>
      </div>
      <div class="table">
        <table>
          <tbody>
              <tr style="border: 1px solid black;height:19pt;">
                  <td>ORÇAMENTO</td>
              </tr>
          </tbody>
      </table>
      {table} 
      </div>
      <div style="margin-top:8px;">
          <table style="border:1px solid black;border-collapse:collapse;width:100%;margin-top: 100pt;">
              <tbody>
                  <tr style="border: 1px solid black;height:19pt;">
                      <td>Subtotal: R$</td>
                      <td>Desconto: R$</td>
                      <td>Acrescimo: R$</td>
                      <td>Total: R${info["total"]}</td>
                  </tr>
              </tbody>
          </table>
      </div>
      
      <div style="margin-top:8px;">
          <table style="border:1px solid black;border-collapse:collapse;width:100%;">
              <tbody>
                  <tr style="border: 1px solid black;height:19pt;" >
                      <td >OBSERVAÇÕES</td>
                  </tr>
                  <tr style="border: 1px solid black;height:83pt;">
                      <td style="text-align: left;">{info["obs"]}</td>
                  </tr>
              </tbody>
          </table>
      </div>
      <p>Os serviços de Entrega e Instalação estão inclusos neste Orçamento. Todos os Preços informados estão expressos em Reais (R$) e são exclusivos a este orçamento. </p>
  </body>
  </html>""")

    pdfkit.from_string(pdf, output_path= "PDF.pdf",configuration= config)
    url = 'PDF.pdf'

    webbrowser.open(url,new=False)



