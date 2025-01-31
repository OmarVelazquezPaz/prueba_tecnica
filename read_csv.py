import pandas as  pd
import os

def delete_blanc_rows(name):
    new_file_name = "new.csv"
    df = pd.read_csv(name)

    mark_isnul = df['company_id'].isnull()
    mark_company_id = df['name'] == 'MiPasajefy'
    df['company_id'] = df['company_id'].fillna('cbf1c8b09cd5b549416d49d220a40cbd317f952e')

    mark_isnul = df['name'].isnull()
    mark_company_id = df['company_id'] == "cbf1c8b09cd5b549416d49d220a40cbd317f952e"

    
    df['name'] = df['name'].fillna('MiPasajefy')
    mark_isnul = df['name'].isnull()

    mark_isnul = df['name'] == 'MiP0xFFFF'
    mark_company_id = df['company_id'] == "cbf1c8b09cd5b549416d49d220a40cbd317f952e"
    df['name'] = df['name'].replace('MiP0xFFFF','MiPasajefy')

    mark_isnul = df['name'] == 'MiPas0xFFFF'
    mark_company_id = df['company_id'] == "cbf1c8b09cd5b549416d49d220a40cbd317f952e"
    df['name'] = df['name'].replace('MiPas0xFFFF','MiPasajefy')

    mark_isnul = df['name'] == 'MiPasajefy'
    mark_company_id = df['company_id'] == "*******"
    df['company_id'] = df['company_id'].replace('*******','cbf1c8b09cd5b549416d49d220a40cbd317f952e')

    mark_isnul = df['name'] == 'MiPasajefy'
    mark_company_id = df['company_id'].isnull()

    
    df['company_id'] = df['company_id'].replace('NaN','cbf1c8b09cd5b549416d49d220a40cbd317f952e')

    

    df.to_csv(new_file_name,index=False)
    print('Done.')
    return new_file_name

def get_columns_names(name):
    with open(name,'r') as f:
        result = f.readline()

    return result


def put_nulls(lst):
    result = [x.split(',') for x in lst]
    for i in range(len(result)):
        if result[i][-1] == '\n':
            result[i][-1] = None
    #print(result)
    return result


def read_all_file(name,nulls=False):
    file = []
    with open(name,'r') as f:
        for line in f:
            file.append(line)
    file.pop(0)
    if nulls:
        file = put_nulls(file)
    return file

def read_file_extracted(name,nulls=False):
    file = []
    with open(name,'r') as f:
        for line in f:
            file.append(line)
    if nulls:
        file = put_nulls(file)
    return file



def all_powers(lst): # quitar
    yield from (l for l in lst)

def write_csv2(lst):
    file_name = "clean.csv"
    with open(file_name,'a') as f:
        f.write(','.join(lst)+'\n')


def write_csv(gen):
    file_name = "extracted.csv"
    with open(file_name,'a') as f:
            f.write(str(next(gen)).strip('[').strip(']') + '\n')
    return file_name



def read_file_to_df(file_name):
    
    with open(file_name,'r') as f:
        print(f.readline())


def clean(split_):
        split_[0] = split_[0].strip().replace("'",'')
        split_[1] = split_[1].strip().replace("'",'')
        split_[2] = split_[2].strip().replace("'",'')
        split_[3] = split_[3].strip().replace("Decimal('",'').replace("')",'')
        split_[4] = split_[4].strip().replace("'",'')
        split_.pop(8)
        split_.pop(8)       
        
        split_[5] = "".join(split_[5:8]).strip().replace("datetime.datetime(",'').replace(')','')
        split_[5] = "".join(split_[5]).replace(' ','-')
        split_.pop(6)       
        split_.pop(6)
        
        if 7 == len(split_):
            split_[6] = 'None'
            
        else:
            split_[6] = "".join(split_[6:9]).strip().replace("datetime.datetime(",'').replace(')','')
            split_[6] = "".join(split_[6]).replace(' ','-')
            split_ = split_[0:7]
        
        
        
        write_csv2(split_)
        
        return split_




if __name__ == '__main__':
    os.system('clear')
    path = 'data_prueba_tecnica.csv'
    # erase blanc rows
    file = delete_blanc_rows(path)
    df = pd.read_csv(path)
    # print(df.head())
    
    
    mark_isnul = df['company_id'].isnull()

    mark_company_id = df['name'] == 'MiPasajefy'

    # df['company_id']  = df['company_id'].replace('NaN','cbf1c8b09cd5b549416d49d220a40cbd317f952e')
    df['company_id'] = df['company_id'].fillna('cbf1c8b09cd5b549416d49d220a40cbd317f952e')
    print(df[mark_isnul & mark_company_id])
    

    








    ########### load ################
    # path = 'data_prueba_tecnica.csv'
    # file = delete_blanc_rows(path)

    # df = [get_columns_names(file)]
    # print(df)
    # content = read_all_file(file)
    # #print(content[0:5])
    # x = [tuple(x.split(',')) for x in content[2:4]]
    # print(x)
    # for record in content[0:5]:
    #     record = tuple(record.split(','))
    #     if len(record) == 6:
    #         record += tuple('null')
    #         print(record)
    #     else:
    #         print(record)
    ########### load ################



    
    