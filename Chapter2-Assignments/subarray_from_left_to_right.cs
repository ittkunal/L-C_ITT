using System;

class Program {
    static void Main(string[] args) {
        var sizeAndQueryCount = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        var elements = Array.ConvertAll(Console.ReadLine().Split(' '), long.Parse);

        var cumulativeSum = new PrefixSumCalculator(elements);
        var queryEvaluator = new QueryEvaluator(cumulativeSum);

        for (var queryCounter = 0; queryCounter < sizeAndQueryCount[1]; queryCounter++) {
            var queryLimits = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            var result = queryEvaluator.CalculateQueryResult(queryLimits[0], queryLimits[1]);
            Console.WriteLine(result);
        }
    }
}

class PrefixSumCalculator {
    private long[] prefixSumArray;

    public PrefixSumCalculator(long[] elements) {
        prefixSumArray = new long[elements.Length + 1];
        prefixSumArray[0] = 0;
        for (int currentIndex = 1; currentIndex <= elements.Length; currentIndex++) {
            prefixSumArray[currentIndex] = prefixSumArray[currentIndex - 1] + elements[currentIndex - 1];
        }
    }

    public long CalculateRangeSum(int left, int right) {
        return prefixSumArray[right] - prefixSumArray[left - 1];
    }
}

class QueryEvaluator {
    private PrefixSumCalculator prefixSumCalculator;

    public QueryEvaluator(PrefixSumCalculator prefixSumCalculator) {
        this.prefixSumCalculator = prefixSumCalculator;
    }

    public long CalculateQueryResult(int left, int right) {
        long sum = prefixSumCalculator.CalculateRangeSum(left, right);
        int length = right - left + 1;
        return sum / length; 
    }
}
