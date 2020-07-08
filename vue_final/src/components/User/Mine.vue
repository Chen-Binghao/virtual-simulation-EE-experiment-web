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
            <h6>Welcome: {{this.Global.loginid}}</h6>
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
          <el-menu-item class="menu_item"><a href="https://www.google.com" target="_blank">小车模拟</a></el-menu-item>

        </el-submenu>


        <el-menu-item index="/User/Mine" ><i class="el-icon-setting"></i>我的</el-menu-item>
      </el-menu>
      <el-row class="tac"></el-row>

      <el-card id="UserDetail">
        <p id="content">用户名：{{this.Global.loginid}}</p>
        <el-divider></el-divider>
<!--        <p id="content">姓名：{{UserDetail.name}}</p>-->
<!--        <el-divider></el-divider>-->
        <p id="content">学号：{{UserDetail.jname}}</p>
        <el-divider></el-divider>
        <p id="content">jaccount：{{UserDetail.ja}}</p>
        <el-divider></el-divider>
        <el-button
          id="start_experiment"
          type="warning"
          icon="el-icon-d-arrow-right"
          round = true
          size="medium"
          :disabled="start_experiment_button"
          :style="{ display: visibleLine}"
        ><el-button id="bound" type="text" ><a :href="this.tobound">jaccount绑定</a></el-button>
        </el-button>
        <el-divider
          :style="{ display: visibleLine}"
        ></el-divider>
        <el-button
          id="start_experiment"
          type="warning"
          icon="el-icon-d-arrow-right"
          round = true
          size="small"
          :disabled="start_experiment_button"
          @click="loginDialogFormVisible = true"
        ><el-button id="bound" type="text" >修改用户名</a></el-button>
        </el-button>
        <el-button
          id="start_experiment"
          type="warning"
          icon="el-icon-d-arrow-right"
          round = true
          size="small"
          :disabled="start_experiment_button"
          @click="loginDialogFormVisible2 = true"
        ><el-button id="bound" type="text" >修改密码</a></el-button>
        </el-button>
        <el-dialog title="修改用户名" :visible.sync="loginDialogFormVisible">
          <el-form ref="loginForm" :model="loginForm" :rules="loginRules">
            <el-form-item label="新用户名" prop="loginid" :label-width="formLabelWidth">
              <el-input v-model="loginForm.loginid" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="resetForm('loginForm')">取 消</el-button>
            <el-button type="primary" @click="editloginid('loginForm')">确 定</el-button>
          </div>
        </el-dialog>
        <el-dialog title="修改密码" :visible.sync="loginDialogFormVisible2">
          <el-form ref="loginForm2" :model="loginForm2" :rules="loginRules2">
            <el-form-item label="新密码" prop="password" :label-width="formLabelWidth">
              <el-input v-model="loginForm2.password" type="password" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="resetForm('loginForm2')">取 消</el-button>
            <el-button type="primary" @click="editpassword()">确 定</el-button>
          </div>
        </el-dialog>
        </el-card>
      <!-- <el-button type="primary" icon="el-icon-edit" @click="companyDialogFormVisible = true"></el-button> -->
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "UserDetail",
    data() {
      return {
        loginDialogFormVisible: false,
        loginDialogFormVisible2: false,
        loginForm: {
          loginid: "",
        },
        loginRules: {
          loginid: [{ required: true, message: "请填写用户名", trigger: "blur" }],
        },
        loginForm2: {
          password: ""
        },
        loginRules2: {
          password: [{ required: true, message: "请填写密码", trigger: "blur" }]
        },
        tobound: '',
        visibleLine: 'none',
        start_experiment_button: false,
        buttonText: "绑定jaccount",
        UserDetail: {
          uname: this.Global.loginid,
          jname: '',
          ja:'',
          name:'',
        },
      };
    },
    created() {
      this.tobound = "https://jaccount.sjtu.edu.cn/oauth2/authorize?response_type=code&state=%23" + this.Global.loginid + "%23&client_id=NLr9Q1f8VaWNxH8xLScIUPO6&redirect_uri=http://202.120.59.222:8022/%23/User/Jaccountbound" + "&scope=basic essential profile";
      this.showUser(this.UserDetail.uname);
    },
    methods: {
      showUser(id) {
        // this.UserDetail.jname = "wei1";
        this.$axios
          .get(this.HOME + "/api/show_user", {
            params: {
              uloginid: this.Global.loginid,
            }
          })
          .then(response => {
            if (response.data.error_num === 0) {
              this.UserDetail.jname = response.data.jname;
              this.UserDetail.name = response.data.name;
              this.UserDetail.ja = response.data.ja;
              if (response.data.jnum === 1){
                this.visibleLine='';
              }
            } else {
              this.$message.error("用户信息加载失败，请重试");
              console.log(response.data.msg);
            }
          });
      },
      editloginid(form) {
        this.$refs[form].validate(valid => {
          if (valid) {
            this.$axios
              .get(this.HOME + "/api/edit_loginid", {
                params: {
                  newloginid: this.loginForm.loginid,
                  oldloginid: this.Global.loginid,
                }
              })
              .then(response => {
                // var res = JSON.parse(response.bodyText);
                if (response.data.error_num === 0) {
                  this.loginDialogFormVisible = false;
                  this.Global.loginid=this.loginForm.loginid,
                  this.$message.success("修改成功");
                } else {
                  this.$message.error("修改失败，可能和其他用户重名，请重试");
                  console.log(response.data.msg);
                }
              });
          } else {
            console.log("error submit!!");
            return false;
          }
        });
      },
      editpassword() {
        this.$axios
          .get(this.HOME + "/api/edit_password", {
            params: {
              uloginid: this.Global.loginid,
              upassword: this.loginForm2.password
            }
          })
          .then(response => {
            if (response.data.error_num === 0) {
              this.loginDialogFormVisible2 = false;
              this.$message.success("修改成功");
            } else {
              this.$message.error("修改失败，请重试");
              console.log(response.data.msg);
            }
          });
      },
      resetForm(form) {
        this.$refs[form].resetFields();
        this.loginDialogFormVisible = false;
        this.loginDialogFormVisible2 = false;
      },
      start_experiment() {
        window.open('https://jaccount.sjtu.edu.cn/oauth2/authorize?response_type=code&client_id=NLr9Q1f8VaWNxH8xLScIUPO6&redirect_uri=http://120.78.123.90:8080/%23/User/Jaccountbound&scope=basic essential profile','_blank');
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
      },
      beforeDestroy() {
        clearInterval(this.timer);
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
  .headText1 {
    position: relative;
    top: -8px;
  }
  .headText2 {
    position: relative;
    top: -5px;
  }
  .image {
    position: absolute;
    width: 60px;
    height: 60px;
    left: 0px;
    top: 0px;
    display: block;
  }
  a:link {
    color:#ffffff;
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

  .basic {
    position: absolute;
    width: 50%;

    top: 20%;
    //bottom: 20px;
    left: 20%;
    //right: 20%;
    padding-left: 5%;
    padding-right: 5%;
  }
  .search {
    width: 60%;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 20%;
    margin-right: 20%;
  }
  #hotSearch {
    font-size: 15px;
    position: relative;
    left: 10%;
  }

  #UserDetail {
    margin-top: 20px;
    margin-bottom: 200px;
    margin-left: 20%;
    margin-right: 41%;
  }

  .el-dialog {
    width: 500px;
    padding-right: 50px;
  }
  #title {
    font-size: 20px;
  }
  #content {
    font-size: 15px;
  }
  #bound {
    color: #8c939d;
  }
</style>
