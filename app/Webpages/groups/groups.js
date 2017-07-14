angular.module("myApp.groups", ['ngRoute', 'angularFileUpload'])
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
        }).when('/groups/info/:groupId/addFiles', {
            templateUrl: 'Webpages/groups/add_files.html',
            controller: 'add_filesController'
        })
    }])

    .controller("groupsController", function ($scope, $http, $routeParams, jwtHelper) {
        if (!localStorage.getItem('token')) {
            window.location.href = '/#!login';
        }
        var token = localStorage.getItem('token');
        $http.defaults.headers.common.Token = token;
        var user_info = jwtHelper.decodeToken(token);
        var id = user_info['id'];
        var data = {
            'user_id': id
        };

        $http.get('http://localhost:5000/groups', data).then(function(response) {
            if(response.data.response === 'error') {
                $scope.error = response.data.error;
            } else {
                $scope.groups = response.data.groups;
            }
        });

        $scope.opengroup = function(id) {
            window.location.href = 'http://localhost:8000/#!/groups/info/' + id;
        }
    })

    .controller("create_groupController", function($scope, $http, jwtHelper) {
        if (!localStorage.getItem('token')) {
            window.location.href = '/#!login';
        }
        $scope.create_group = function create_group(group){
            $scope.token = localStorage.getItem('token');
            var token = jwtHelper.decodeToken($scope.token);
            if($scope.token) {
                $http.defaults.headers.common.Token = $scope.token;
                var data = {
                    'description': group.description,
                    'name': group.name,
                    'admin': token['id']
                };

                $http.post('http://localhost:5000/groups', data).then(function(response){
                    if(response.data.response === "error"){
                        $scope.error = response.data.error;
                    } else {
                        $scope.success = response.data.success;
                    }
                })
            }

            else {
                window.location.href = 'http://localhost:8000/#!/login';
            }
        }
    })
    //TODO: Finish group info page.
    .controller("group_infoController", function($scope, $http, $routeParams, jwtHelper) {
        if (!localStorage.getItem('token')) {
            window.location.href = '/#!login';
        }
        var group_id = $routeParams['groupId'];

        $http.get('http://localhost:5000/group/' + group_id).then(function (response) {
            $scope.groups = response.data;
            console.log(response);
        });

        $scope.send_invite = function(invitation) {
            var group_id = $routeParams['groupId'];
            data = {
                'group_id': group_id,
                'user_name': invitation.user_name
            };
            $http.post('http://localhost:5000/invites', data).then(function(response) {
                if(response.data.response === "error"){
                    $scope.error = response.data.error;
                } else {
                    $scope.success = response.data.success;
                }

            });
        }
    })

    .controller("add_filesController", function ($scope, $http, $routeParams, jwtHelper, FileUploader) {


        //$scope.resource = {};

        var uploader = $scope.uploader = new FileUploader({
            url: "http://localhost:5000/documents",
            queueLimit: 1
        });

        uploader.onSuccessItem = function (fileItem) {
            console.log("uploaded file");
        }
});
