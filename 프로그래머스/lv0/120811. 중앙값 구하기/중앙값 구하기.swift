import Foundation

func solution(_ array:[Int]) -> Int {
    //var space = [Any]()
    var space = [Int]()
    space = array.sorted()
    
    return space[((space.count) / 2)]
}
