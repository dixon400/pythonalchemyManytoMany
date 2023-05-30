from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, company_dev, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # query = session.query(company_dev, Company, Dev). \
    # join(Company, company_dev.c.company_id == Company.id). \
    # join(Dev, company_dev.c.dev_id == Dev.id). \
    # order_by(company_dev.c.company_id)

    
    query = session.query(company_dev, Company, Dev). \
    join(Company, company_dev.c.company_id == Company.id). \
    join(Dev, company_dev.c.dev_id == Dev.id). \
    filter(company_dev.c.company_id == 2). \
    order_by(company_dev.c.company_id)

    freebie = session.query(Freebie).first()
    for attribute, value in vars(freebie).items():
        print(f"{attribute}: {value}")
    dev = freebie.dev
    company = freebie.company

    print(freebie.print_details())
    print(dev, company)
    print('-_-_-')
    results = query.all()

    for result in results:
        print(result)

    for row in results:
        company_id = row[0]
        dev_id = row[1]
        company_name = row[2].name
        dev_name = row[3].name
        print(f"Company ID: {company_id}, Company Name: {company_name}, Dev ID: {dev_id}, Dev Name: {dev_name}")
        print('---')