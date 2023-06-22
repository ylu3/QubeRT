from bisect import bisect_right
from typing import List
from models.contract import Contract
from models.optimize_result import OptimizeResult


class Scheduling:
    @staticmethod
    def contract_scheduling(contracts: List[Contract]) -> OptimizeResult:
        """
        Calculates the maximum profit for a given list of contract scheduling and returns selected jobs.
        Args:
            contracts (List[Contract]): A list of contracts with start time, duration, price, and name.

        Returns:
            OptimizeResult: A named tuple with the maximum profit and the selected contracts.
        """
        # Separate the attributes of contracts into separate lists for easier processing
        start_times, end_times, prices, names = zip(*[(contract.start, contract.start + contract.duration,
                                                       contract.price, contract.name) for contract in contracts])

        index = list(range(len(contracts)))
        # Sort the contracts based on end times
        index.sort(key=lambda x: end_times[x])
        # Initialize lists for storing previous end times and maximum profit
        pre, dp = [0], [(0, [])]

        for i in index:
            # Find the latest contract that ends before the current contract starts
            j = bisect_right(pre, start_times[i]) - 1
            # Calculate the current profit by either adding the price of the current contract to the previous maximum
            # profit or taking the previous maximum profit
            new_profit = dp[j][0] + prices[i]
            if new_profit > dp[-1][0]:
                cur = (new_profit, dp[j][1] + [names[i]])
            else:
                cur = dp[-1]
            # Append the current profit and the current contract's end time
            dp.append(cur)
            pre.append(end_times[i])

        # Return the maximum profit obtained and the jobs list
        return OptimizeResult(income=dp[-1][0], path=sorted(dp[-1][1]))
