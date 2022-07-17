"use strict";

const openbbBP = document.querySelector(".bb-bench-press-modal"); //flat bb bench press
const bbbpModal = document.querySelector(".bbbp-modal");

const openibbBP = document.querySelector(".inc-bench-press-modal"); //incline bb bench press
const ibbbpModal = document.querySelector(".ibbbp-modal");

const openLCP = document.querySelector(".landmine-chest-press-modal"); //landmine press
const lcpModal = document.querySelector(".lcp-modal");

const openDCP = document.querySelector(".decline-chest-press-modal"); //decline bb press
const dcpModal = document.querySelector(".dcp-modal");

const openDBP = document.querySelector(".db-press-modal"); //flat db press
const dbpModal = document.querySelector(".dbp-modal");

const openCGBP = document.querySelector(".cg-bench-press-modal"); //close grip press
const cgbpModal = document.querySelector(".cgbp-modal");

const openUHPF = document.querySelector(".underhand-pec-fly-modal"); //underhand pec fly
const uhpfModal = document.querySelector(".uhpf-modal");

const openPF = document.querySelector(".pec-fly-modal"); //pectoral fly
const pfModal = document.querySelector(".pf-modal");

const openIDBP = document.querySelector(".inc-db-press-modal"); //incline dumbbell press
const idbpModal = document.querySelector(".idbp-modal");

const openDBPULL = document.querySelector(".db-pullover-modal");
const dbpullModal = document.querySelector(".dbpull-modal");

const openLTOHCF = document.querySelector(".ltoh-cablefly-modal");
const ltohcfModal = document.querySelector(".ltohcf-modal");

const openHTOLCF = document.querySelector(".htol-cablefly-modal");
const htolcfModal = document.querySelector(".htolcf-modal");

const openMLCF = document.querySelector(".ml-cablefly-modal");
const mlcfModal = document.querySelector(".mlcf-modal");

const openSARCP = document.querySelector(".sa-rot-chest-press-modal");
const sarcpModal = document.querySelector(".sarcp-modal");

const overlay = document.querySelector(".overlay");
const closeBtnModal = document.querySelectorAll(".close-modal");

const openModal = function (event) {
  let temp = event.currentTarget.classList.value;
  if (temp === "bb-bench-press-modal") {
    bbbpModal.classList.remove("hidden");
  } else if (temp === "inc-bench-press-modal") {
    ibbbpModal.classList.remove("hidden");
  } else if (temp === "landmine-chest-press-modal") {
    lcpModal.classList.remove("hidden");
  } else if (temp === "decline-chest-press-modal") {
    dcpModal.classList.remove("hidden");
  } else if (temp === "db-press-modal") {
    dbpModal.classList.remove("hidden");
  } else if (temp === "cg-bench-press-modal") {
    cgbpModal.classList.remove("hidden");
  } else if (temp === "underhand-pec-fly-modal") {
    uhpfModal.classList.remove("hidden");
  } else if (temp === "pec-fly-modal") {
    pfModal.classList.remove("hidden");
  } else if (temp === "inc-db-press-modal") {
    idbpModal.classList.remove("hidden");
  } else if (temp === "db-pullover-modal") {
    dbpullModal.classList.remove("hidden");
  } else if (temp === "ltoh-cablefly-modal") {
    ltohcfModal.classList.remove("hidden");
  } else if (temp === "htol-cablefly-modal") {
    htolcfModal.classList.remove("hidden");
  } else if (temp === "ml-cablefly-modal") {
    mlcfModal.classList.remove("hidden");
  } else if (temp === "sa-rot-chest-press-modal") {
    sarcpModal.classList.remove("hidden");
  }
  overlay.classList.remove("hidden");
};

openibbBP.addEventListener("click", openModal);
openbbBP.addEventListener("click", openModal);
openDBP.addEventListener("click", openModal);
openDCP.addEventListener("click", openModal);
openLCP.addEventListener("click", openModal);
openCGBP.addEventListener("click", openModal);
openUHPF.addEventListener("click", openModal);
openPF.addEventListener("click", openModal);
openIDBP.addEventListener("click", openModal);
openDBPULL.addEventListener("click", openModal);
openLTOHCF.addEventListener("click", openModal);
openHTOLCF.addEventListener("click", openModal);
openMLCF.addEventListener("click", openModal);
openSARCP.addEventListener("click", openModal);

const closeModal = function (event) {
  bbbpModal.classList.add("hidden");
  ibbbpModal.classList.add("hidden");
  lcpModal.classList.add("hidden");
  dcpModal.classList.add("hidden");
  dbpModal.classList.add("hidden");
  cgbpModal.classList.add("hidden");
  uhpfModal.classList.add("hidden");
  pfModal.classList.add("hidden");
  idbpModal.classList.add("hidden");
  dbpullModal.classList.add("hidden");
  ltohcfModal.classList.add("hidden");
  htolcfModal.classList.add("hidden");
  mlcfModal.classList.add("hidden");
  sarcpModal.classList.add("hidden");
  overlay.classList.add("hidden");
};

for (let i = 0; i < closeBtnModal.length; i++) {
  closeBtnModal[i].addEventListener("click", closeModal);
}
overlay.addEventListener("click", closeModal);
