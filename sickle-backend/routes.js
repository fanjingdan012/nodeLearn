
exports.setRequestUrl=function(app){
    var userController = require('./Controllers/UserController')
        ,indexObj = require('./controllers/index')
        ,fileObj = require('./controllers/fileSystem')
        ,mongoObj = require('./controllers/mongoManagement')
        ,articleObj = require('./controllers/article')
        ,personController = require('./Controllers/PersonController');


    
    app.get('/Persons', personController.list);
    app.post('/Person',personController.create);

    app.post('/User', userController.create);
    app.get('/Users', userController.list);
    app.get('/User/userManager', userController.userManager);
    app.get('/', userController.login);
    app.post('/onLogin', userController.onLogin);

    app.post('/index/newContent', indexObj.newContent);
    app.get('/index', indexObj.index);
    app.get('/index/:id', indexObj.viewContect);
    app.get('/index/:id/edit', indexObj.editContect);
    app.post('/index/:id/edit', indexObj.saveContect);
    app.get('/index/:id/delete', indexObj.deleteContectById);

    app.all("/mongo/index",mongoObj.index);

    app.get("/file/*",fileObj.initFileInfo)
    app.get("/fileBrowser/pdf/*",fileObj.initPdf)


    //  app.get("/article/articleManager",articleObj.initManager);
    app.get("/article/articleManager/:articleId?",articleObj.initManager);
    app.get("/article/articleDetail/:articleId?",articleObj.articleDetail);
    app.get("/article/articleItem",articleObj.articleItem);
    app.all("/article/search",articleObj.search)

    app.post("/article/saveArticleType",articleObj.saveArticleType);
    app.post("/article/saveArticleDetail",articleObj.saveArticleDetail);
    app.get("/article/listContext",articleObj.listContextPage);
    app.get("/article/articleTypeAll",articleObj.articleTypeAll);



}