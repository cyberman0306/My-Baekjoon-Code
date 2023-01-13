import Foundation

func solution(_ numbers:[Int]) -> Int {
    var space = [Int]()
    space = numbers
    var a:Int = 0
    var b:Int = 0
    var z:Int = 0
    for i in space {
        if a < i {
            a = i
        }
    }
    z = space.firstIndex(of: a)!
    space.remove(at: z)
    for j in space {
        if b < j {
            b = j
        }
    }
    return a * b
}