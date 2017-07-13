angular.module("myApp.groups", ['ngRoute'])
    .config(['$routeProvider', function($routeProvider){
        $routeProvider.when('/groups', {
            templateUrl: 'Webpages/groups/groups.html',
            controller: 'groupsController'
        }).when('/groups/create', {
            templateUrl: 'Webpages/groups/create_group.html',
            controller: 'create_groupController'
        }).when('/groups/info/:groupId', {
            templateUrl: 'Webpages/groups/group_info.html',
            controller: 'group_infoController'
        })
    }])

    .controller("groupsController", function ($scope, $http, $routeParams) {
        $scope.username = localStorage.getItem('username');
        $scope.userid = localStorage.getItem('userid');

        $scope.signout = function signout(){
            localStorage.clear();
            $http.defaults.headers.common.Token = null;
        };

        $http({
            method: 'GET',
            url: 'http://localhost:5000/groups/' + $scope.userid
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
            console.log(response);
        }, function errorCallback(response) {
            console.log(response);
        })
    })

    .controller("create_groupController", function($scope, $http) {
        $scope.create_group = function create_group(group){
            var data = {
                'description': group.description,
                'name': group.name,
                'admin': 'lol'
            }
        }
    })
    //TODO: Finish group info page.
    .controller("group_infoController", function($scope, $http, $routeParams) {
        groupId = $routeParams['groupId'];
        console.log(groupId);

        $http({
            method: 'GET',
            url: 'http://localhost:5000/group/' + groupId
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
            console.log(response);
        }, function errorCallback(response) {
            console.log(response);
        })
    });

