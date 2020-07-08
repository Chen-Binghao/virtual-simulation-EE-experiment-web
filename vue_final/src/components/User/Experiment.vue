<template>
  <div>
    <el-container direction="vertical">
      <el-row class="top-bar">
        <img src="../../assets/lable1.png" class="image" />
        <el-col :span="3" :offset="2">
          <div class="headText1" @click="backToMain">
            <h4>远程虚拟仿真实验</h4>
          </div>
        </el-col>
        <el-col :span="3">
          <div class="headText2">
            <h6>by 第二大组</h6>
          </div>
        </el-col>
        <el-col :span="2">
          <div class="headText2">
            <h6>Welcome: {{this.a}}</h6>
          </div>
        </el-col>
        <el-col :span="1" :offset="10">
          <el-button id="exit" type="primary" @click="backToLogin">退出登录</el-button>
        </el-col>
      </el-row>

      <div class="line"></div>
      <el-menu
        :default-active="$route.path"
        class="menu"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#ffffff"
        active-text-color="#ffd04b"
        router
      >
        <el-menu-item index="/User/Experiment" ><i class="el-icon-menu"></i>实验列表</el-menu-item>

        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-location"></i>其他功能
          </template>
          <el-menu-item class="menu_item"><a href="http://202.120.59.222:8004/upload/" target="_blank">行人检测AI系统</a></el-menu-item>
          <el-menu-item class="menu_item"><a href="../../../static/CarMaze/maze.html" target="_blank">小车模拟</a></el-menu-item>

        </el-submenu>


        <el-menu-item index="/User/Mine" ><i class="el-icon-setting"></i>我的</el-menu-item>
      </el-menu>
      <el-row class="tac"></el-row>

      <div v-if="labList.length>0">
        <el-card class="searchResult" v-for="(job, index) in labList" :key="index">
          <el-link type="primary" @click="labDetail(job.pk)">{{job.fields.labname}}</el-link>
          <p>
            <span>{{job.fields.intro}}</span>
          </p>
        </el-card>
      </div>

    </el-container>
  </div>
</template>


<script>
  export default {
    name: "experiment",
    data() {
      return {
        a: '',
        labList: [
          {
            pk: "1",
            fields: {
              labname: "little car",
              intro: "car simulation test",
            }
          },
          {
            pk: "2",
            fields: {
              labname: "electric circuit experiment 1",
              intro: "the first test",
            }
          },
          {
            pk: "3",
            fields: {
              labname: "electric circuit experiment 2",
              intro: "the second test",
            }
          },
          {
            pk: "4",
            fields: {
              labname: "electric circuit experiment 3",
              intro: "the third test",
            }
          },
          {
            pk: "5",
            fields: {
              labname: "electric circuit experiment 4",
              intro: "the fourth test",
            }
          }
        ]
      };
    },
    created() {
      this.a=this.Global.loginid
      let url = window.location.href
      if (url.split('=')[1] !== undefined) {
        let code = url.split('=')[1]
        console.log(code)
        console.log(this.HOME)
        this.Global.code="grant_type=authorization_code&code=" + code + "&redirect_uri=http://202.120.59.222:8022/%23/User/Experiment&client_id=NLr9Q1f8VaWNxH8xLScIUPO6&client_secret=67CB621520E5FD52EA984983DC19CB4FDAF25B83FEE51F52"
        this.gettoken(this.Global.code)
      }
    },
    methods: {
      labDetail(id) {
        this.$router.push({
          path: "/User/ExperimentDetail",
          query: { eid: id }
        });
      },
      gettoken(code) {
        this.$axios(
          {
            method:'post',
            baseURL: '/jac',
            url: '/oauth2/token?'+code,
            headers:{
              'Content-Type': 'application/x-www-form-urlencoded;',
              'Authorization': 'Basic'
            },
            data:{}
          }
        )
        .then(res=>{
          this.token=res.data['id_token']
          console.log(this.token)
          let jwt = require('jsonwebtoken')
          let str = jwt.decode(this.token)
          console.log(str['code'])
          this.$axios
            .get(this.HOME + "/api/jaccount_login", {
              params: {
                uj: str['code'],
                uname: str['sub'],
              }
            })
            .then(response => {
              // var res = JSON.parse(response.bodyText);
              if (response.data.error_num === 2) {
                this.$message.error("注册失败，可能存在同名用户，请重试");
                console.log(response.data.msg);
              } else {
                this.loginDialogFormVisible = false;
                if(response.data.error_num === 0) {
                  this.$message.success("登录成功");
                  this.a=response.data.uloginid;
                  this.Global.loginid=response.data.uloginid;
                } else {
                  this.$message.success("已注册新用户，账号密码均为您的学号");
                  this.a=response.data.uloginid;
                  this.Global.loginid=response.data.uloginid;
                }
              }
            });
        })
      },
      backToMain() {
        this.$router.push({ path: "/User/Experiment" });
      },
      backToLogin() {
        this.Global.loginid = "";
        this.$router.push({ path: "/" });
      },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  };
</script>

<style lang="scss" scoped>
  .top-bar {
    background: #646e77;
    color: white;
    a {
      color: white;
    }
    height: 60px;
  }
  .image {
    position: absolute;
    width: 60px;
    height: 60px;
    left: 0px;
    top: 0px;
    display: block;
  }
  .headText1 {
    position: relative;
    top: -8px;
  }
  .headText2 {
    position: relative;
    top: -5px;
  }
  #exit {
    position: relative;
    top: 15px;
    background-color: transparent;
    border: 0;
  }
  .menu {
    padding-left: 20%;
    padding-right: 20%;
  }

  .searchResult {
    width: 50%;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 20%;
    margin-right: 20%;
    padding-left: 5%;
    padding-right: 5%;
    font-size: 15px;
  }

  .basic {
    width: 50%;
    margin-top: 40px;
    margin-bottom: 20px;
    margin-left: 20%;
    margin-right: 20%;
    padding-left: 5%;
    padding-right: 5%;
  }
  .button {
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 45%;
  }

  .el-dialog {
    width: 500px;
    padding-right: 50px;
  }

  a:link {
    color: #ffffff;
    text-decoration:none;
  }
  a:visited {
    color:#ffffff;
    text-decoration:none;
  }
  a:hover {
    color:#ffffff;
    text-decoration:none;
  }
  a:active {
    color:#ffffff;
    text-decoration:none;
  }

  #title {
    font-size: 20px;
  }
  #content {
    font-size: 15px;
  }
</style>
