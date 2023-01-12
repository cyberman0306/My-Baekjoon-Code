import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    var a = 0
    var b = 0
    
    for i in array {
        if i == n {
            b += 1
        }
    }
    return b
}