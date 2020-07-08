<template>
  <div>
    <el-card class="login_card">
      <img src="../assets/online_lab.jpg" class="image" />
      <el-button type="text" @click="loginDialogFormVisible = true">点击注册</el-button>
      <el-button type="text" @click="loginDialogFormVisible2 = true">点击登录</el-button>
      <el-button type="text" ><a href="https://jaccount.sjtu.edu.cn/oauth2/authorize?response_type=code&client_id=NLr9Q1f8VaWNxH8xLScIUPO6&redirect_uri=http://202.120.59.222:8022/%23/User/Experiment&scope=basic essential profile">jaccount登录</a></el-button>
      <el-dialog title="用户注册" :visible.sync="loginDialogFormVisible">
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules">
          <el-form-item label="用户名" prop="loginid" :label-width="formLabelWidth">
            <el-input v-model="loginForm.loginid" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password" :label-width="formLabelWidth">
            <el-input v-model="loginForm.password" type="password" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="resetForm('loginForm')">取 消</el-button>
          <el-button type="primary" @click="addUser('loginForm')">确 定</el-button>
        </div>
      </el-dialog>
      <el-dialog title="用户登录" :visible.sync="loginDialogFormVisible2">
        <el-form ref="loginForm2" :model="loginForm2" :rules="loginRules2">
          <el-form-item label="用户名" prop="loginid" :label-width="formLabelWidth">
            <el-input v-model="loginForm2.loginid" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password" :label-width="formLabelWidth">
            <el-input v-model="loginForm2.password" type="password" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="resetForm('loginForm2')">取 消</el-button>
          <el-button type="primary" @click="loginUser()">确 定</el-button>
        </div>
      </el-dialog>
    </el-card>
  </div>
</template>


<script>
  export default {
    name: "Login",
    data() {
      return {
        loginDialogFormVisible: false,
        loginDialogFormVisible2: false,
        loginDialogFormVisible3: false,
        loginForm: {
          loginid: "",
          password: "",
        },
        loginRules: {
          loginid: [{ required: true, message: "请填写用户名", trigger: "blur" }],
          password: [{ required: true, message: "请填写密码", trigger: "blur" }],
        },
        loginForm2: {
          loginid: "",
          password: ""
        },
        loginRules2: {
          loginid: [{ required: true, message: "请填写用户名", trigger: "blur" }],
          password: [{ required: true, message: "请填写密码", trigger: "blur" }]
        },
        loginForm3: {
          loginid: "",
          password: ""
        },
        loginRules3: {
          loginid: [{ required: true, message: "请填写用户名", trigger: "blur" }],
          password: [{ required: true, message: "请填写密码", trigger: "blur" }]
        },
        checkList: [],
        formLabelWidth: "100px"
      };
    },
    methods: {
      addUser(form) {
        this.$refs[form].validate(valid => {
          if (valid) {
            this.$axios
              .get(this.HOME + "/api/add_user", {
                params: {
                  uloginid: this.loginForm.loginid,
                  upassword: this.loginForm.password,
                }
              })
              .then(response => {
                // var res = JSON.parse(response.bodyText);
                if (response.data.error_num === 0) {
                  this.loginDialogFormVisible = false;
                  this.$message.success("注册成功");
                } else {
                  this.$message.error("新增用户失败，请重试");
                  console.log(response.data.msg);
                }
              });
          } else {
            console.log("error submit!!");
            return false;
          }
        });
      },
      loginUser() {
        this.$axios
          .get(this.HOME + "/api/user_login", {
            params: {
              uloginid: this.loginForm2.loginid,
              upassword: this.loginForm2.password
            }
          })
          .then(response => {
            if (response.data.error_num === 0) {
              this.Global.loginid = this.loginForm2.loginid;
              this.$router.push({
                path: "/User/Experiment"
              });
            } else {
              this.$message.error("密码错误或用户不存在，请重试");
              console.log(response.data.msg);
            }
          });
      },
      resetForm(form) {
        this.$refs[form].resetFields();
        this.loginDialogFormVisible = false;
        this.loginDialogFormVisible2 = false;
        this.loginDialogFormVisible3 = false;
      },
    }
  };
</script>

<style>
  .image {
    width: 100%;
    height: 255px;
    display: block;
  }
  .login_card {
    position: absolute;
    left: 550px;
    top: 150px;
    width: 400px;
    height: 320px;
  }
  .el-dialog {
    width: 500px;
    padding-right: 50px;
  }
</style>
