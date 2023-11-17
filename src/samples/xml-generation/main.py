from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    converter = CSVtoXMLConverter("/data/fifa_23.csv")
    xml_str = converter.to_xml_str()  # Obtém a representação XML como string

    # Escreve a string XML em um arquivo
    with open("/data/fifa_23.xml", "w") as xml_file:
        xml_file.write(xml_str)

    print("Arquivo XML 'fifa_23.xml' criado com sucesso!")



    