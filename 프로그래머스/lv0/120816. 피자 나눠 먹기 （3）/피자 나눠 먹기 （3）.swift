import Foundation

func solution(_ slice:Int, _ n:Int) -> Int {
    var a:Int = 0
    var b:Int = 0
    
    for a in 1...100 {
        if (a * slice) / n > 0 {
            b = a
            break
        }
    }
    
    return b
}
