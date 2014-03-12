/**
 * Created by yash on 3/11/2014.
 */
function classController($scope, $http){
    $http.get('api/v1/class/?format=json').success(function(data) {
        console.log(data.objects[0].students);
        var stuff = data.objects[0].students;
        $scope.stuff = stuff;
    }).error(function(data){
        //this code will execrute if get fails
    });
}
