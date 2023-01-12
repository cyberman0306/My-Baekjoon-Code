import Foundation

func solution(_ numer1:Int, _ denom1:Int, _ numer2:Int, _ denom2:Int) -> [Int] {
    let top = (numer1*denom2) + (numer2*denom1)
    
    let bot = denom1*denom2
    
    var max = 1
    
    for i in 1...top {
        if top % i == 0 && bot % i == 0 {
            max = i
        }
    }
    return [top/max, bot/max]
}
