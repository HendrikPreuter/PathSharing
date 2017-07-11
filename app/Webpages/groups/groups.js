angular.module("myApp", []).controller("groupsController", function($scope, $http) {
    $http({
        method: 'GET',
        url: 'http://localhost:5000/groups/1'
    }).then(function successCallback(response) {
        $scope.jsVar = response.data;
        console.log(response);
    }, function errorCallback(response) {
        console.log(response);
    })
});