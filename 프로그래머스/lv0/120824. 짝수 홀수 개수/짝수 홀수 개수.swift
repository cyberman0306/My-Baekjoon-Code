import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var a:Int = 0
    var b:Int = 0
    for i in num_list {
        if i % 2 == 0 {
            a += 1
        } else {
            b += 1
        }
    }
    return [a, b]
}
