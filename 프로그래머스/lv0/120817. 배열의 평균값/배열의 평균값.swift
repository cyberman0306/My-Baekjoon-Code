import Foundation

func solution(_ numbers:[Int]) -> Double {
    var a: Int = 0
    for i in numbers {
        a += i
        
    }
    return Double(a) / Double(numbers.count)
}
