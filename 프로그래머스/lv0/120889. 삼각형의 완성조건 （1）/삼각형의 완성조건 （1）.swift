import Foundation

func solution(_ sides:[Int]) -> Int {
    var big:Int = 0
    var a = 0
    var space = [Int]()
    space = sides
    big = space.max()!
    a = space.firstIndex(of: big)!
    space.remove(at: a)
    if space[0] + space[1] > big {
        return 1
    } else {
        return 2
    }
}