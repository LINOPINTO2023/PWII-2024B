
public class CoinJar {
    private int coinCount;
    private static int totalCoins = 0;
    public static final int METRIC_TARGET = 1000;

    public CoinJar() {
        coinCount = 0;
    }

    public void insertCoin() {
        System.out.println("\nclink\n");
        coinCount++;
        totalCoins++;
        if (totalCoins >= METRIC_TARGET) {
            System.out.println("Time to go shopping!\n");
        }
    }

    public int getCoinCount() {
        return coinCount;
    }

    public static int getTotalCoins() {
        return totalCoins;
    }
}