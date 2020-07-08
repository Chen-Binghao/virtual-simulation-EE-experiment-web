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
          <el-menu-item class="menu_item"><a href="../../../static/CarMaze/maze.html" target="_blank">小车模拟</a></el-menu-item>

        </el-submenu>


        <el-menu-item index="/User/Mine" ><i class="el-icon-setting"></i>我的</el-menu-item>
      </el-menu>
      <el-row class="tac"></el-row>

      <el-card id="ExperimentDetail">
        <p id="title">{{ExperimentDetail.ename}}</p>
        <p id="content">实验编号：{{ExperimentDetail.eid}}</p>
        <el-divider></el-divider>
        <p id="content">实验名称：{{ExperimentDetail.ename}}</p>
        <el-divider></el-divider>
        <p id="content">实验内容：{{ExperimentDetail.econtent}}</p>
        <el-divider></el-divider>
        <p id="content">实验成绩：{{ExperimentDetail.egrade}}</p>
        <el-divider></el-divider>
        <el-button
          id="start_experiment"
          type="warning"
          icon="el-icon-d-arrow-right"
          :disabled="start_experiment_button"
          @click="start_experiment()"
        >{{buttonText}}</el-button>
        <el-button
                :style="{display:this.visible}"
                id="start_result"
                type="warning"
                icon="el-icon-d-arrow-right"
                :disabled="start_result_button"
                @click="start_result()"
          >{{"前往答题"}}</el-button>
      </el-card>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "ExperimentDetail",
    data() {
      return {
        start_experiment_button: false,
        start_result_button: false,
        buttonText: "前往实验",
        detailurl:'',
        resulturl:'',
        visible:'',
        ExperimentDetail: {
          eid: "1",
          ename: "",
          econtent: "",
          egrade: "",
        },
      };
    },
    created() {
      this.ExperimentDetail.eid = this.$route.query.eid;
      if(this.$route.query.eid==='1')
      {
        this.detailurl='../../../static/CarMaze/maze.html';
        this.resulturl='Score';
        this.visible='none';
      }
      else if(this.$route.query.eid==='2')
      {
        this.detailurl='http://tinyurl.com/yafwa2k7';
        this.resulturl='Ex1';
      }else if(this.$route.query.eid==='3')
      {
        this.detailurl='http://tinyurl.com/y7bj55nq';
        this.resulturl='Ex2';
      }else if(this.$route.query.eid==='4')
      {
        this.detailurl='http://tinyurl.com/yakbr8vl';
        this.resulturl='Ex3';
      }else
      {
        this.detailurl='http://lushprojects.com/circuitjs/circuitjs.html?cct=$+1+0.000005+10.20027730826997+50+5+43%0As+384+80+448+80+0+0+false%0Av+384+80+224+80+0+0+40+15+0+0+0.5%0Aw+448+80+448+256+0%0Aw+416+256+448+256+0%0AS+416+256+368+256+0+0+false+0+2%0Aw+224+80+144+80+0%0Aw+368+240+144+240+0%0Ar+144+80+144+240+0+100%0Aw+144+80+64+80+0%0Ap+64+144+64+240+1+0%0Aw+64+240+144+240+0%0Aw+144+240+144+272+0%0A370+144+272+368+272+1+0%0As+64+80+64+144+0+0+false%0A';
        this.resulturl='Ex4';
      }
      this.showExperiment(this.ExperimentDetail.eid);
    },
    methods: {
      showExperiment(id) {
        this.$axios
          .get(this.HOME + "/api/show_experiment", {
            params: {
              uloginid: this.Global.loginid,
              eid: id
            }
          })
          .then(response => {
            if (response.data.error_num === 0) {
              this.ExperimentDetail.ename = response.data.ename;
              this.ExperimentDetail.econtent = response.data.econtent;
              this.ExperimentDetail.egrade = response.data.egrade;
            } else {
              this.$message.error("获取数据失败，请重试");
              console.log(response.data.msg);
            }
          });
      },
      start_experiment() {
        window.open(this.detailurl,'_blank');
      },
      start_result() {
        this.$router.push({ path: "/User/" + this.resulturl});
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
  #ExperimentDetail {
    margin-top: 20px;
    margin-bottom: 200px;
    margin-left: 20%;
    margin-right: 41%;
  }
  #companyInfo {
    position: absolute;
    top: 120px;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 60%;
    margin-right: 20%;
  }
  #start_experiment {
    position: absolute;
    top: 550px;
    left: 310px;
  }
  #start_result {
    position: absolute;
    top: 550px;
    left: 450px;
  }
  #title {
    font-size: 25px;
  }
  #content {
    font-size: 15px;
  }
  #title2 {
    font-size: 15px;
  }
  #content2 {
    font-size: 12px;
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
</style>
