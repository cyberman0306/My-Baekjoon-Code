import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    
    var a = [Int]()
    
    for i in numbers {
        a.append(i * 2)
    }
            
    return a
}
