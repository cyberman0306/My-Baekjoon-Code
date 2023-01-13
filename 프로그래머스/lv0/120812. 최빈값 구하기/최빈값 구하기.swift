import Foundation

func solution(_ array:[Int]) -> Int {
    var counter: [Int: Int] = [:]
    array.forEach { counter[$0] = (counter[$0] ?? 0) + 1 }

    let result = counter.filter { $0.value == counter.values.max() }
    return result.count == 1 ? result.first!.key : -1
}