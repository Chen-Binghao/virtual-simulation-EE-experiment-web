<template>
  <div>
    <el-col :span="5">
    <p >请计算出结果并填写在下方:</p>
      <p >A:</p>
    <el-input v-model = "a" type = "primary" id = "a" ></el-input>
    <p >Ri(Kohm):</p>
    <el-input v-model = "ri" type = "primary" id = "ri" ></el-input>
    <p >Ro(Kohm):</p>
    <el-input v-model = "ro" type = "primary" id = "ro" ></el-input></el-col>
    <el-button type="primary" id="submit" icon="el-icon-d-arrow-right" @click="submit(a,ri,ro)">submit</el-button>
  </div>
</template>

<script>
  export default {
    name: "score",
    data() {
      return {
        a: "",
        ri: "",
        ro: "",
        score: 0,
        formLabelWidth: "100px"
      };
    },
    created() {

    },
    methods: {
      submit(a, ri, ro) {
        this.score=0
        if(a>=36 && a<=51)
          this.score += 40
        if(ri>=4.5 && ri<=5.5)
          this.score += 30
        if(ro>=1.8 && ro<=2.2)
          this.score += 30

        this.$axios
          .get(this.HOME + "/api/ex_score", {
            params: {
              eid: '4',
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
