import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    var a:Int = 0
    a = n / 10
    
    return (k - a) * 2000 + (n * 12000)
}