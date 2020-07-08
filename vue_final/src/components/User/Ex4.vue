<template>
  <div>
    <el-col :span="8">
    <p >请回答以下问题（是1,否0）</p>
      <p >正常运行时K1，K2，K3是否闭合（K2填触点）:</p>
    <el-input v-model = "b1" type = "primary" id = "b1" ></el-input>
    <p >故障测量时K1，K2，K3是否闭合（K2填触点）:</p>
    <el-input v-model = "b2" type = "primary" id = "b2" ></el-input>
    <p >根据电压电流表读数判断是否开路，是否短路:</p>
    <el-input v-model = "b3" type = "primary" id = "b3" ></el-input></el-col>
    <el-button type="primary" id="submit" icon="el-icon-d-arrow-right" @click="submit(b1,b2,b3)">submit</el-button>
  </div>
</template>

<script>
  export default {
    name: "score",
    data() {
      return {
        b1: "",
        b2: "",
        b3: "",
        score: 0,
        formLabelWidth: "100px"
      };
    },
    created() {

    },
    methods: {
      submit(b1, b2, b3) {
        this.score=0
        if(b1==='110')
          this.score+=30
        if(b2==='121')
          this.score+=30
        if(b3==='00')
          this.score+=40
        this.$axios
          .get(this.HOME + "/api/ex_score", {
            params: {
              eid: '5',
              uloginid: this.Global.loginid,
              uscore: this.score.toString(),
            }
          })
        this.$router.push({ path: "/User/Experiment" });
    }}
  };
</script>

<style lang="scss" scoped>
  #submit{
    position: absolute;
    top: 325px;
    left: 10px;
  }
  .button {
    background: transparent;
    color: transparent;
    position: absolute;
    margin-top: 500px;
    margin-bottom: 500px;
    margin-left: 45%;
    padding-left: 0%;
    padding-right: 0%;
    padding-left: -5px;
    padding-right: 6%;
  }
</style>
