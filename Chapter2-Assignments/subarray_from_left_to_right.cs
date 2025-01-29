using System;

class Program {
    static void Main(string[] args) {
        var (elements, queryCount) = ReadInput();
        var cumulativeSum = new PrefixSumCalculator(elements);
        var queryEvaluator = new QueryEvaluator(cumulativeSum);

        ProcessQueries(queryEvaluator, queryCount);
    }

    private static (long[], int) ReadInput() {
        var sizeAndQueryCount = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        var elements = Array.ConvertAll(Console.ReadLine().Split(' '), long.Parse);
        return (elements, sizeAndQueryCount[1]);
    }

    private static void ProcessQueries(QueryEvaluator queryEvaluator, int queryCount) {
        for (var queryCounter = 0; queryCounter < queryCount; queryCounter++) {
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
