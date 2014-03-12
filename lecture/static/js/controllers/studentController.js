/**
 * Created by yash on 3/11/2014.
 */

function studentController($scope, $http) {
    $http.get('api/v1/student/?format=json').success(function(data){
        console.log(data);

    }).error(function(data){
        //this code will execute if our Get fails
    });
    $scope.user = {"klass": "api/v1/class/1/", 'project':[]};

    $scope.addStudent = function(){
        console.log($scope.user);
        alert('wait');
        $http.post('api/v1/student/', $scope.user).success(function(){
    });
  }
};