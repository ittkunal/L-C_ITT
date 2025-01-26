public class Customer
{
    public int CustomerID { get; set; }
    public string CompanyName { get; set; }
    public string ContactName { get; set; }
    public string Country { get; set; }
}

public class CustomerSearch
{
    private readonly DatabaseContext db; 

    public CustomerSearch(DatabaseContext context)
    {
        db = context;
    }

    // Search customer by Country
    public List<Customer> SearchByCountry(string country)
    {
        var query =
            from customer in db.customers
            where customer.Country.Contains(country)
            orderby customer.CustomerID ascending
            select customer;

        return query.ToList();
    }

    // Search customer by CompanyName
    public List<Customer> SearchByCompanyName(string company)
    {
        var query =
            from customer in db.customers
            where customer.CompanyName.Contains(company)
            orderby customer.CustomerID ascending
            select customer;

        return query.ToList();
    }

    // Search customer by ContactPerson
    public List<Customer> SearchByContact(string contact)
    {
        var query =
            from customer in db.customers
            where customer.ContactName.Contains(contact)
            orderby customer.CustomerID ascending
            select customer;

        return query.ToList();
    }
}

public class CustomerExporter
{
    public string ExportToCSV(List<Customer> customerRecordList)
    {
        StringBuilder csvbuilder = new StringBuilder();

        foreach (var customerRecord in customerRecordList)
        {
            csvbuilder.AppendFormat("{0},{1},{2},{3}", customerRecord.CustomerID, customerRecord.CompanyName, customerRecord.ContactName, customerRecord.Country);
            csvbuilder.AppendLine();
        }

        return csvbuilder.ToString();
    }
}
