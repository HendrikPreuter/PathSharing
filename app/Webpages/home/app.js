angular.module("myApp", []).controller("myController", ['$scope', '$http', function($scope, $http) {
    try{
        $scope.token = localStorage.getItem('token');
        console.log($scope.id, $scope.username);
        if($scope.token){
            $scope.id = $scope.token['id'];
            $scope.username = $scope.token['username'];
        }
    } catch(Exception) {
        console.log(Exception);
    }
}]);