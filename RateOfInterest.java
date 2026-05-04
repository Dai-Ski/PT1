    class RBI {
        double rateOfInterest() {
            return 7.0;
        }
    }
    class HDFC extends RBI{
        @Override
        double rateOfInterest() {
            return 8.5;
        }
    }
    class ICICI extends RBI{
        @Override
        double rateOfInterest() {
        return 7.8;
    }
    }
public class RateOfInterest {
    public static void main(String[] args) {
        RBI rbi = new RBI();
        System.out.println("RBI Interest Rate: " + rbi.rateOfInterest());

        RBI hdfc = new HDFC();
        System.out.println("HDFC Interest Rate: " + hdfc.rateOfInterest());
        
        RBI icici = new ICICI();
        System.out.println("ICICI Interest Rate: " + icici.rateOfInterest());
    }
}