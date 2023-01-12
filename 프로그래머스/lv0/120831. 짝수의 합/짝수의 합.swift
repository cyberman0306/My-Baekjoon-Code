import Foundation

func solution(_ n:Int) -> Int {
    var a: Int = 0
    for i in 1...n {
        if i % 2 == 0 {
            a += i
        }
    }
    
    return a
}