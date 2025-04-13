public class Customer {

    private String firstName;
    private String lastName;
    private Wallet myWallet;

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public Wallet getWallet() {
        return myWallet;
    }

    
    public boolean makePayment(float amount) {
        if (myWallet.hasSufficientFunds(amount)) {
            myWallet.subtractMoney(amount);
            return true;
        }
        return false;
    }
}

class Wallet {

    private float value;

    public float getTotalMoney() {
        return value;
    }

    public void setTotalMoney(float newValue) {
        value = newValue;
    }

    public void addMoney(float deposit) {
        value += deposit;
    }

    public void subtractMoney(float debit) {
        value -= debit;
    }

    public boolean hasSufficientFunds(float amount) {
        return value >= amount;
    }
}
