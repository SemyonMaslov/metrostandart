import re


def collection_data(text):
    buff_measuring_instrument = re.findall(r"(?<=;).*?(?=Рег)", text)[0]
    measuring_instrument = buff_measuring_instrument.replace(
        'наименование и обозначение типа, модификация (при наличии) средства измерений, регистрационный номер в',
        '')
    buff_facts = re.findall(r"(?<=факторов:).*?(?=и на основании)", text)[0]
    facts = buff_facts.replace(
        'перечень влияющих факторов, при которых проводилась поверка, с указанием их значений',
        '')
    data = {
        'date': re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text),
        'verification':
            re.findall(r"(?<= СВИДЕТЕЛЬСТВО О ПОВЕРКЕ ).*?(?=Действительно)",
                       text)[0],
        'verifier': re.findall(r"(?<=Поверитель ).*?(?=фамилия)", text)[
            0],
        'measuring_instrument': measuring_instrument,
        'factory_number':
            re.findall(r"(?<=заводской номер).*?(?=заводской )", text)[0],
        'accordance':
            re.findall(r"(?<=поверки в соответствии с).*?(?=наименование или)",
                       text)[0],
        'facts': facts,
    }
    return data 
