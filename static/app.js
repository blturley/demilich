const $usernav = $("#user-nav-btn");
const $charnav = $("#character-nav-btn" );
const $abilitynav = $("#ability-nav-btn" );
const $equipnav = $("#equipped-nav-btn");
const $itemnav = $("#item-nav-btn");
const $newcharbtn = $("#new-char-btn");
const $addweaponbtn = $("#add-weapon-btn");
const $additembtn = $("#add-item-btn");
const $addabilitybtn = $("#add-ability-btn");
const $gravebtn = $("#grave-container");
const $charscroll = $("#character-scroll");
const $infocontainer = $("#info-container");
const $userinfo = $("#user-info");
const $charcontainer = $("#character-template-container");
const $charinfo = $("#character-info");
const $chareditbtn = $("#character-edit-btn" );
const $chardeletebtn = $("#character-delete-btn");
const $killbtn = $(".kill-button");
const $iteminfo = $("#item-info");
const $equippedlist = $("#equipped-item-list");
const $unequippedlist= $("#unequipped-item-list");
const $abilitieslist = $("#abilities-item-list");
const $itemsbtns = $("#items-buttons");
const $abilitiesbtns = $("#abilities-buttons");
const $equipbox = $("#equipment-box");
const $equippedbox = $("#equipped-box");
const $unequippedbox = $("#unequipped-box");
const $abilitybox = $("#ability-box");
const $addcharform = $("#add-character-form-container");
const $addabilityform = $("#add-ability-form-container");
const $addweaponform = $("#add-weapon-form-container");
const $additemform = $("#add-item-form-container");
const $characterbaricons = $(".character-bar-icon");
const $editformcontainer = $("#edit-form-container");
const $currcharportrait = $("#curr-character-portrait");
const $chardeleteshowbtn = $('#character-delete');
const $chardeletemenu = $('#character-delete-buttons');
const $charsubmitdelete = $("#character-delete-submit");
const $characterbar = $('#character-bar-container')
const $graveyard = $('#graveyard-container')
const $helpbtn = $('#help-btn')
const $helpinfo = $('#help-info')
const $introinfo = $('#intro-info')
const $deactivateshow = $('#deactivate-btn')
const $accountdeletemenu = $('#account-delete-buttons')
const $accountdeletecancel = $('#account-delete-cancel')

let currcharacter;
let currability;
let currequipped;
let currunequipped;
let currwindow;

const url = "http://127.0.0.1:5000";


/* ------------------------CYCLE THROUGH MENUS------------------------ */

function hideAll() {
    $userinfo.hide();
    $charinfo.hide();
    $iteminfo.hide();
    $equippedlist.hide();
    $unequippedlist.hide();
    $abilitieslist.hide();
    $itemsbtns.hide();
    $abilitiesbtns.hide();
    $addcharform.hide();
    $addabilityform.hide();
    $addweaponform.hide();
    $additemform.hide();
    $abilitybox.hide();
    $equippedbox.hide();
    $unequippedbox.hide();
    $editformcontainer.hide();
    $chardeletemenu.hide();
    $graveyard.hide();
    $helpinfo.hide();
    $introinfo.hide();
    $accountdeletemenu.hide();
};

$charscroll.on("click", ".character-bar-icon", function() {
    hideAll();
    $infocontainer.show();
    $charinfo.show();
    currwindow = "character";
});
$usernav.on("click", function() {
    hideAll();
    $infocontainer.show();
    $userinfo.show();
});
$charnav.on("click", function() {
    if (currcharacter) {
        hideAll();
        $charinfo.show();
        currwindow = "character";
    }
});
$abilitynav.on("click", function() {
    if (currcharacter) {
        hideAll();
        $iteminfo.show();
        $abilitiesbtns.show();
        $abilitieslist.show();
        $abilitybox.show();
        currwindow = "ability";
    }
});
$equipnav.on("click", function() {
    if (currcharacter) {
        hideAll();
        $iteminfo.show();
        $equippedlist.show();
        $itemsbtns.show();
        $equippedbox.show();
        currwindow = "equipped";
    }
});
$itemnav.on("click", function() {
    if (currcharacter) {
        hideAll();
        $iteminfo.show();
        $unequippedlist.show();
        $itemsbtns.show();
        $unequippedbox.show();
        currwindow = "unequipped";
    }
});
$newcharbtn.on("click", function() {
    hideAll();
    $infocontainer.show();
    $addcharform.show();
});
$addabilitybtn.on("click", function() {
    hideAll();
    $addabilityform.show();
});
$addweaponbtn.on("click", function() {
    hideAll();
    $addweaponform.show();
});
$additembtn.on("click", function() {
    hideAll();
    $additemform.show();
});
$chardeleteshowbtn.on("click", function() {
    hideAll();
    $chardeletemenu.show();
});
$chardeleteshowbtn.on("click", function() {
    hideAll();
    $chardeletemenu.show();
});
$helpbtn.on("click", function() {
    hideAll();
    $infocontainer.show();
    $helpinfo.show();
});
$deactivateshow.on("click", function() {
    hideAll();
    $accountdeletemenu.show();
});
$accountdeletecancel.on("click", function() {
    hideAll();
    $userinfo.show();
});




/* ------------------------GRAVEYARD BUTTON PRESS------------------------ */

$gravebtn.on("click", function() {
    hideAll();
    let innergrave = $('#grave-cards').html()
    if (!(innergrave.includes("card"))){
        $('#grave-cards').html('<span class="card-text character-info-entry mt-5">You have no dead characters.</span>');
    }
    $graveyard.show();
    $infocontainer.show();
})



/* ------------------------KILL BUTTON PRESS------------------------ */

$killbtn.on("click", function() {
    location.assign(`${url}/deathform/${currcharacter.data.character.id}`)
})



/* ------------------------CHANGE FORM PORTRAIT/ICON PREVIEWS------------------------ */

$("#portrait_url").on("change", function() {
    $("#character-portrait-preview").css("background-image", `url(${$("#portrait_url").val()})`);
});

$("#icon").on("change", function() {
    $("#character-icon-preview").css("background-image", `url(${$("#icon").val()})`);
});

$addabilityform.on("change", "#image_url", function(event) {
    $targ = $(event.target);
    $("#ability-icon-preview").css("background-image", `url(${$targ.val()})`);
})
$addweaponform.on("change", "#image_url", function(event) {
    $targ = $(event.target);
    $("#weapon-icon-preview").css("background-image", `url(${$targ.val()})`);
});
$additemform.on("change", "#image_url", function(event) {
    $targ = $(event.target);
    $("#item-icon-preview").css("background-image", `url(${$targ.val()})`);
});
$editformcontainer.on("change", "#image_url", function(event){
    $targ = $(event.target);
    $("#edit-form-container .icon-container-large").css("background-image", `url(${$targ.val()})`);
})
$editformcontainer.on("change", "#portrait_url", function(event){
    $targ = $(event.target);
    $("#edit-form-container #character-portrait-preview").css("background-image", `url(${$targ.val()})`);
})
$editformcontainer.on("change", "#icon", function(event){
    $targ = $(event.target);
    $("#edit-form-container #character-icon-preview").css("background-image", `url(${$targ.val()})`);
})



/* ------------------------UPDATE AFTER CHARACTER SELECT------------------------ */

async function changecharinfo(char) {
    $('#character-info-name').html(char.name)
    $('#lvl-race-class').html(`lvl ${char.level} ${char.race} ${char.class_name}`)
    $('#character-info-alignment').html(char.alignment)
    $('#character-info-age').html(char.age)
    $('#character-info-stats').html(char.stats)
    $('#character-info-proficiencies').html(char.proficiencies)
    $('#character-info-statuses').html(char.statuses)
    $('#character-info-languages').html(char.languages)
    $('#character-info-traits').html(char.traits)
    $('#character-info-hirelings').html(char.hirelings)
    $('#character-info-pets-minions').html(char.pets_minions)
    $('#character-info-backstory').html(char.backstory)
    $('#character-info-notes').html(char.notes)
    $currcharportrait.css("background-image", `url(${char.portrait_url})`)
}


async function changeabilitieslist(char) {
    $abilitieslist.html("");
    for (val in char.data.abilities) {  
        $abilitieslist.append(
            `<span class="item-li dl-text" data-itemtype="ability" data-id="${char.data.abilities[val].id}">
            ${char.data.abilities[val].name}
            </span>
            <br>`)
    };
}

async function changeitemslists(char) {
    $equippedlist.html("");
    $unequippedlist.html("");
    for (val in char.data.weapons) { 
        if (char.data.weapons[val].is_equipped){
            $equippedlist.append(
                `<span class="item-li dl-text" data-itemtype="weapon" data-id="${char.data.weapons[val].id}" 
                data-equipped="true">
                ${char.data.weapons[val].name}
                </span>
                <br>`);
        }
        else {
            $unequippedlist.append(
                `<span class="item-li dl-text" data-itemtype="weapon" data-id="${char.data.weapons[val].id}" 
                data-equipped="false">
                ${char.data.weapons[val].name}
                </span>
                <br>`);
        }
    };
    for (val in char.data.items) { 
        if (char.data.items[val].is_equipped){
            $equippedlist.append(
                `<span class="item-li dl-text" data-itemtype="item" data-id="${char.data.items[val].id}" 
                data-equipped="true">
                ${char.data.items[val].name}
                </span>
                <br>`);
        }
        else {
            $unequippedlist.append(
                `<span class="item-li dl-text" data-itemtype="item" data-id="${char.data.items[val].id}" 
                data-equipped="false">
                ${char.data.items[val].name}
                </span>
                <br>`);
        }
    };
}

$characterbar.on("click", ".character-bar-icon", async function(event) {
    $('#character-scroll .character-bar-icon').removeClass('char-bar-active');
    $targ = $(event.target);
    $targ.addClass('char-bar-active');
    currcharacter = await axios.get(`${url}/character/${$targ.attr("data-id")}`);
    await changecharinfo(currcharacter.data.character);
    await changeabilitieslist(currcharacter);
    await changeitemslists(currcharacter);
    $abilitybox.html("");
    $equippedbox.html("");
    $unequippedbox.html("");
});



/* ------------------------UPDATE AFTER ABILITY/ITEM SELECT------------------------ */

$iteminfo.on("click", ".item-li", async function(event) {
    $targ = $(event.target);

    if ($targ.attr("data-itemtype") == "ability") {
        $("#abilities-item-list .item-li").removeClass("dl-list-active");
        currability = $targ;
        let currhtml = await axios.get(`${url}/ability/${$targ.attr("data-id")}`);
        await $abilitybox.html(currhtml.data);
    }
    else if ($targ.attr("data-equipped") == "true") {
        $("#equipped-item-list .item-li").removeClass("dl-list-active");
        if ($targ.attr("data-itemtype") == "weapon") {
            currequipped = $targ;
            let currhtml = await axios.get(`${url}/weapon/${$targ.attr("data-id")}`);
            await $equippedbox.html(currhtml.data);
        }
        else {
            currequipped = $targ;
            let currhtml = await axios.get(`${url}/item/${$targ.attr("data-id")}`);
            await $equippedbox.html(currhtml.data);
        }
    }   
    else {
        $("#unequipped-item-list .item-li").removeClass("dl-list-active");
        if ($targ.attr("data-itemtype") == "weapon") {
            currunequipped = $targ;
            let currhtml = await axios.get(`${url}/weapon/${$targ.attr("data-id")}`);
            await $unequippedbox.html(currhtml.data);
        }
        else {
            currunequipped = $targ;
            let currhtml = await axios.get(`${url}/item/${$targ.attr("data-id")}`);
            await $unequippedbox.html(currhtml.data);
        }
    }

    $targ.addClass('dl-list-active');
});



/* ------------------------SHOW EDIT FORMS------------------------ */

$charcontainer.on("click", ".edit-btn", async function() {
    hideAll();
    
    if (currwindow == "character") {
        let currhtml = await axios.get(`${url}/geteditcharacter/${currcharacter.data.character.id}`);
        $editformcontainer.html(currhtml.data);
    }
    if (currwindow == "ability") {
        let currhtml = await axios.get(`${url}/geteditability/${currability.attr("data-id")}`);
        $editformcontainer.html(currhtml.data);
    }
    if (currwindow == "equipped") {
        let currhtml;
        if (currequipped.attr("data-itemtype") == "weapon") {
            currhtml = await axios.get(`${url}/geteditweapon/${currequipped.attr("data-id")}`);
        }
        else {
            currhtml = await axios.get(`${url}/getedititem/${currequipped.attr("data-id")}`);
        }
        $editformcontainer.html(currhtml.data);
    }
    if (currwindow == "unequipped") {
        let currhtml;
        if (currunequipped.attr("data-itemtype") == "weapon") {
            currhtml = await axios.get(`${url}/geteditweapon/${currunequipped.attr("data-id")}`);
        }
        else {
            currhtml = await axios.get(`${url}/getedititem/${currunequipped.attr("data-id")}`);
        }
        $editformcontainer.html(currhtml.data);
    }

    $("#edit-form-container .errorbox").html("");
    $editformcontainer.show();
});



/* ------------------------SUBMIT DELETE CHARACTER------------------------ */

$charsubmitdelete.click(async function(e) {
    await axios({
        method: "delete",
        url: `${url}/deletecharacter/${currcharacter.data.character.id}`
    });

    $('.char-bar-active').remove();

    hideAll();
    $infocontainer.hide();

    currcharacter = null;
});



/* ------------------------SUBMIT DELETE ABILITY/ITEM------------------------ */

$iteminfo.on("click", ".delete-btn", async function() {


    if (currwindow == "ability") {
        await axios({
            method: "delete",
            url: `${url}/deleteability/${currability.attr("data-id")}`
        });

        currcharacter = await axios.get(`${url}/character/${currcharacter.data.character.id}`);

        currability.remove();
        await changeabilitieslist(currcharacter);
    
        $abilitybox.html("");
    }

    if (currwindow == "equipped") {

        if (currequipped.attr("data-itemtype") == "weapon"){
            await axios({
                method: "delete",
                url: `${url}/deleteweapon/${currequipped.attr("data-id")}`
            });
        }
        else if (currequipped.attr("data-itemtype") == "item"){
            await axios({
                method: "delete",
                url: `${url}/deleteitem/${currequipped.attr("data-id")}`
            });
        }

        currcharacter = await axios.get(`${url}/character/${currcharacter.data.character.id}`);

        currequipped.remove();
        await changeitemslists(currcharacter);
 
        $equippedbox.html(""); 
    }

    if (currwindow == "unequipped") {

        if (currunequipped.attr("data-itemtype") == "weapon"){
            await axios({
                method: "delete",
                url: `${url}/deleteweapon/${currunequipped.attr("data-id")}`
            });
        }
        else if (currunequipped.attr("data-itemtype") == "item"){
            await axios({
                method: "delete",
                url: `${url}/deleteitem/${currunequipped.attr("data-id")}`
            });
        }

        currcharacter = await axios.get(`${url}/character/${currcharacter.data.character.id}`);

        currunequipped.remove();
        await changeitemslists(currcharacter);
 
        $unequippedbox.html(""); 
    }
});



/* ------------------------NEW CHARACTER FORM SUBMIT------------------------ */

$('#add-char-form').submit(async function(e) {
    e.preventDefault();

    let newchar = await axios({
        method: "post",
        url: `${url}/newcharacter`,
        data: $('#add-char-form').serialize()
    });

    if (newchar.data.errors) {
        let errors = newchar.data.errors
        for (error in errors) {
            await $("#new-character-errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    }

    $characterbaricons.removeClass('char-bar-active');

    await $('#character-scroll').append(
    `<img src="${newchar.data.icon}" class="character-bar-icon char-bar-active" 
    alt="character icon" data-id="${newchar.data.id}"></img>)`)

    hideAll();

    currcharacter = await axios.get(`${url}/character/${newchar.data.id}`);

    currwindow = "character";

    await changecharinfo(currcharacter.data.character);
    $abilitieslist.html("");
    $equippedlist.html("");
    $unequippedlist.html("");
    $abilitybox.html("");
    $equippedbox.html("");
    $unequippedbox.html("");

    $charinfo.show();
});



/* ------------------------NEW ABILITY/ITEM FORM SUBMIT------------------------ */

$('#add-ability-form').submit(async function(e) {
    e.preventDefault();

    let newability = await axios({
        method: "post",
        url: `${url}/newability/${currcharacter.data.character.id}`,
        data: $('#add-ability-form').serialize()
    });

    if (newability.data.errors) {
        let errors = newability.data.errors
        for (error in errors) {
            await $("#new-ability-errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    }

    await $abilitieslist.append(
        `<span class="item-li dl-text" data-itemtype="ability" data-id="${newability.data.id}">
        ${newability.data.name}
        </span>
        <br>`);

    hideAll();
    $iteminfo.show();
    $abilitiesbtns.show();
    $abilitieslist.show();
    $abilitybox.show();
});

$('#add-weapon-form').submit(async function(e) {
    e.preventDefault();

    let newweapon = await axios({
        method: "post",
        url: `${url}/newweapon/${currcharacter.data.character.id}`,
        data: $('#add-weapon-form').serialize()
    });

    if (newweapon.data.errors) {
        let errors = newweapon.data.errors
        for (error in errors) {
            await $("#new-weapon-errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    }

    if (newweapon.data.is_equipped) {

        await $equippedlist.append(
            `<span class="item-li dl-text" data-itemtype="weapon" data-equipped="true" data-id="${newweapon.data.id}">
            ${newweapon.data.name}
            </span>
            <br>`);
        
        hideAll();
        $iteminfo.show();
        $equippedlist.show();
        $itemsbtns.show();
        $equippedbox.show();
        currwindow = "equipped";
    }
    else {

        await $unequippedlist.append(
            `<span class="item-li dl-text" data-itemtype="weapon" data-equipped="false" data-id="${newweapon.data.id}">
            ${newweapon.data.name}
            </span>
            <br>`);

        hideAll();
        $iteminfo.show();
        $unequippedlist.show();
        $itemsbtns.show();
        $unequippedbox.show();
        currwindow = "unequipped";
    }
});

$('#add-item-form').submit(async function(e) {
    e.preventDefault();

    let newitem = await axios({
        method: "post",
        url: `${url}/newitem/${currcharacter.data.character.id}`,
        data: $('#add-item-form').serialize()
    });

    await console.log(newitem);

    if (newitem.data.errors) {
        let errors = newitem.data.errors
        for (error in errors) {
            await $("#new-item-errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    }

    if (newitem.data.is_equipped) {

        await $equippedlist.append(
            `<span class="item-li dl-text" data-itemtype="item" data-equipped="true" data-id="${newitem.data.id}">
            ${newitem.data.name}
            </span>
            <br>`);
        
        hideAll();
        $iteminfo.show();
        $equippedlist.show();
        $itemsbtns.show();
        $equippedbox.show();
        currwindow = "equipped";
    }
    else {

        await $unequippedlist.append(
            `<span class="item-li dl-text" data-itemtype="item" data-equipped="false" data-id="${newitem.data.id}">
            ${newitem.data.name}
            </span>
            <br>`);

        hideAll();
        $iteminfo.show();
        $unequippedlist.show();
        $itemsbtns.show();
        $unequippedbox.show();
        currwindow = "unequipped";
    }
});



/* ------------------------EDIT CHARACTER FORM SUBMIT------------------------ */

$('#edit-form-container').submit("#edit-char-form", async function(e) {
    e.preventDefault();

    if (currwindow !== "character") {
        return;
    }

    let newchar = await axios({
        method: "patch",
        url: `${url}/editcharacter/${currcharacter.data.character.id}`,
        data: $('#edit-form-container #edit-char-form').serialize()
    });

    if (newchar.data.errors) {
        let errors = newchar.data.errors
        for (error in errors) {
            await $("#edit-form-container .errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    }

    hideAll();

    await changecharinfo(newchar.data);

    $("#character-scroll .char-bar-active").attr("src", `${newchar.data.icon}`);

    $charinfo.show();
});



/* ------------------------EDIT ABILIY/ITEMS FORM SUBMIT------------------------ */

$('#edit-form-container').submit("#edit-ability-form", async function(e) {
    e.preventDefault();

    if (currwindow !== "ability") {
        return;
    }

    let newability = await axios({
        method: "patch",
        url: `${url}/editability/${currability.attr("data-id")}`,
        data: $('#edit-form-container #edit-ability-form').serialize()
    });

    if (newability.data.errors) {
        let errors = newability.data.errors
        for (error in errors) {
            await $("#edit-form-container .errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    }

    let currhtml = await axios.get(`${url}/ability/${currability.attr("data-id")}`);
    currability.text(newability.data.name)
    await $abilitybox.html(currhtml.data);
    hideAll();
    $iteminfo.show();
    $abilitiesbtns.show();
    $abilitieslist.show();
    $abilitybox.show();
});


$('#edit-form-container').submit("#edit-weapon-form", async function(e) {
    e.preventDefault();

    if (currwindow !== "equipped" && currwindow !== "unequipped") {
        return;
    }

    let newweapon;
    let currhtml;

    if (currwindow == "equipped") {

        if (currequipped.attr("data-itemtype") !== "weapon")
            return;

        newweapon = await axios({
            method: "patch",
            url: `${url}/editweapon/${currequipped.attr("data-id")}`,
            data: $('#edit-form-container #edit-weapon-form').serialize()
        });

        currhtml = await axios.get(`${url}/weapon/${currequipped.attr("data-id")}`);
    }
    else {

        if (currunequipped.attr("data-itemtype") !== "weapon")
            return;

        newweapon = await axios({
            method: "patch",
            url: `${url}/editweapon/${currunequipped.attr("data-id")}`,
            data: $('#edit-form-container #edit-weapon-form').serialize()
        });

        currhtml = await axios.get(`${url}/weapon/${currunequipped.attr("data-id")}`);
    }

    if (newweapon.data.errors) {
        let errors = newweapon.data.errors
        for (error in errors) {
            await $("#edit-form-container .errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    } 
    if (currwindow == "equipped"){
        await $equippedbox.html(currhtml.data);
        currequipped.text(newweapon.data.name)
        hideAll();
        $iteminfo.show();
        $equippedlist.show();
        $itemsbtns.show();
        $equippedbox.show();
    } 
    else {
        await $unequippedbox.html(currhtml.data);
        currunequipped.text(newweapon.data.name)
        hideAll();
        $iteminfo.show();
        $unequippedlist.show();
        $itemsbtns.show();
        $unequippedbox.show();
    }
});


$('#edit-form-container').submit("#edit-item-form", async function(e) {
    e.preventDefault();

    if (currwindow !== "equipped" && currwindow !== "unequipped") {
        return;
    }

    let newitem;
    let currhtml;

    if (currwindow == "equipped") {

        if (currequipped.attr("data-itemtype") !== "item")
            return;

        newitem = await axios({
            method: "patch",
            url: `${url}/edititem/${currequipped.attr("data-id")}`,
            data: $('#edit-form-container #edit-item-form').serialize()
        });

        currhtml = await axios.get(`${url}/item/${currequipped.attr("data-id")}`);
    }
    else {

        if (currunequipped.attr("data-itemtype") !== "item")
            return;

        newitem = await axios({
            method: "patch",
            url: `${url}/edititem/${currunequipped.attr("data-id")}`,
            data: $('#edit-form-container #edit-item-form').serialize()
        });

        currhtml = await axios.get(`${url}/item/${currunequipped.attr("data-id")}`);
    }

    if (newitem.data.errors) {
        let errors = newitem.data.errors
        for (error in errors) {
            await $("#edit-form-container .errorbox").html(
                `<span class="dl-text" style="color:red;">${error}: ${errors[error]}</span>
                <br>`);
        }
        return;
    } 
    if (currwindow == "equipped"){
        await $equippedbox.html(currhtml.data);
        currequipped.text(newitem.data.name)
        hideAll();
        $iteminfo.show();
        $equippedlist.show();
        $itemsbtns.show();
        $equippedbox.show();
    } 
    else {
        await $unequippedbox.html(currhtml.data);
        currunequipped.text(newitem.data.name)
        hideAll();
        $iteminfo.show();
        $unequippedlist.show();
        $itemsbtns.show();
        $unequippedbox.show();
    }
});



/* ------------------------ITEM/WEAPON EQUIP & UNEQUIP------------------------ */

$iteminfo.on("click", ".unequip-btn", async function() {
    if(currequipped.attr("data-itemtype") == "weapon"){
        currhtml = await axios.patch(`${url}/weaponunequip/${currequipped.attr("data-id")}`);
    }
    else {
        currhtml = await axios.patch(`${url}/itemunequip/${currequipped.attr("data-id")}`);
    }

    currequipped = null;
    currunequipped = null;

    currcharacter = await axios.get(`${url}/character/${currcharacter.data.character.id}`);

    await changeitemslists(currcharacter);
    $equippedbox.html("");
    $unequippedbox.html("");
});


$iteminfo.on("click", ".equip-btn", async function() {
    if(currunequipped.attr("data-itemtype") == "weapon"){
        currhtml = await axios.patch(`${url}/weaponequip/${currunequipped.attr("data-id")}`);
    }
    else {
        currhtml = await axios.patch(`${url}/itemequip/${currunequipped.attr("data-id")}`);
    }

    currequipped = null;
    currunequipped = null;

    currcharacter = await axios.get(`${url}/character/${currcharacter.data.character.id}`);

    await changeitemslists(currcharacter);
    $equippedbox.html("");
    $unequippedbox.html("");
});



/* ------------------------COPY ABILITY/ITEM------------------------ */

$iteminfo.on("click", ".copy-drop", async function(event) {
    event.preventDefault();
    $targ = $(event.target);
    let resp;

    let charid = $targ.attr("data-charid");
    let itemid = $targ.attr("data-itemid");
    let itemtype = $targ.attr("data-itemtype");

    resp = await axios.get(`${url}/copyitem`, { params: { charid, itemid, itemtype } });

    $("#item-info .copy-box").html("<span class='dl-text' style='color: green;'>Copy successful!</span>")
});



/* ------------------------GET 5E ABILITIES/ITEMS------------------------ */

$(".spell-drop").on("click", async function(event) {
    event.preventDefault();
    $targ = $(event.target);

    resp = await axios.get(`https://www.dnd5eapi.co/api/spells/${$targ.attr("data-index")}`);

    await $('#add-ability-form #name').val(resp.data.name);

    await $('#add-ability-form #description').val(resp.data.desc);

    if (resp.data.attack_type){
    await $('#add-ability-form #effect_area').val(resp.data.attack_type);
    }
    else {
        await $('#add-ability-form #effect_area').val("N/A");
    }

    if (resp.data.damage.damage_at_character_level){
        let str = "damage at character level,";
        for (let val in resp.data.damage.damage_at_character_level){
            str += val;
            str += " ";
            str += resp.data.damage.damage_at_character_level[val];
            str += ",";
            str += " ";
        }
        await $('#add-ability-form #damage').val(str);
    }
    else if (resp.data.damage.damage_at_slot_level){
        let str = "damage at slot level,";
        for (let val in resp.data.damage.damage_at_slot_level){
            str += val;
            str += " ";
            str += resp.data.damage.damage_at_slot_level[val];
            str += ",";
            str += " ";
        }
        await $('#add-ability-form #damage').val(str);
    }
    else if (resp.data.heal_at_slot_level){
        let str = "heal at slot level,";
        for (let val in resp.data.heal_at_slot_level){
            str += val;
            str += " ";
            str += resp.data.heal_at_slot_level[val];
            str += ",";
            str += " ";
        }
        await $('#add-ability-form #damage').val(str);
    }
    else if (resp.data.heal_at_character_level){
        let str = "heal at character level, ";
        for (let val in resp.data.heal_at_character_level){
            str += val;
            str += " ";
            str += resp.data.heal_at_character_level[val];
            str += ",";
            str += " ";
        }
        await $('#add-ability-form #damage').val(str);
    }
    else{
        $('#add-ability-form #damage').val("N/A");
    }
    if (resp.data.damage) {
        await $('#add-ability-form #damage_type').val(resp.data.damage.damage_type.name);
    }
    else {
        await $('#add-ability-form #damage_type').val("N/A");
    }
    await $('#add-ability-form #min_level').val(resp.data.level);

    await $('#add-ability-form #ability_range').val(resp.data.range);

    await $('#add-ability-form #school').val(resp.data.school.name);

    if (resp.data.casting_time) {
        await $('#add-ability-form #notes').val("Casting Time: " + resp.data.casting_time + " " + resp.data.higher_level);
    }
    else {
        await $('#add-ability-form #notes').val(resp.data.higher_level);
    }

    $('#add-ability-form #is_spell').prop("checked", true);
});


$(".skill-drop").on("click", async function(event) {
    event.preventDefault();
    $targ = $(event.target);

    resp = await axios.get(`https://www.dnd5eapi.co/api/skills/${$targ.attr("data-index")}`);

    await $('#add-ability-form #name').val(resp.data.name);
    await $('#add-ability-form #description').val(resp.data.desc);
    await $('#add-ability-form #ability_range').val("N/A");
    await $('#add-ability-form #school').val("N/A");
    await $('#add-ability-form #min_level').val(1);
    await $('#add-ability-form #damage_type').val("N/A");
    await $('#add-ability-form #damage').val("N/A");
    await $('#add-ability-form #effect_area').val("N/A");
    if (resp.data.ability_score) {
        await $('#add-ability-form #notes').val("Ability Score: " + resp.data.ability_score.name);
    }
    
    $('#add-ability-form #is_spell').prop("checked", false);
});


$(".weapon-drop").on("click", async function(event) {
    event.preventDefault();
    $targ = $(event.target);

    resp = await axios.get(`https://www.dnd5eapi.co${$targ.attr("data-url")}`);

    let res = await resp.data;

    await $('#add-weapon-form #name').val(res.name);

    if (res.damage) {
    
        await $('#add-weapon-form #weapon_range').val(res.weapon_range);
        await $('#add-weapon-form #weight').val(res.weight);
        await $('#add-weapon-form #damage_type').val(res.damage.damage_type.name);
        await $('#add-weapon-form #weapon_type').val(res.weapon_category);
        await $('#add-weapon-form #rarity').val("N/A");
        await $('#add-weapon-form #condition').val("Good");

        if (res['2h_damage']) {
            let dam = await res['2h_damage']
            let str = "1h: ";
            str += await res.damage.damage_dice;
            str += ",";
            str += " ";
            str += "2h: ";
            str += await dam.damage_dice;
            await $('#add-weapon-form #damage').val(str);
        }
        else {
            await $('#add-weapon-form #damage').val(res.damage.damage_dice);
        }

        if (resp.data.cost) {
            await $('#add-weapon-form #notes').val("Cost: " + res.cost.quantity + res.cost.unit);
        }
        if (res.properties){
            propstr = "Properties: "
            for (let prop of res.properties) {
                propstr += prop.name
                propstr += ","
                propstr += " "
            }
            await $('#add-weapon-form #description').val(propstr);
        }
        else {
            await $('#add-weapon-form #description').val("weapon");
        }
    }
    else {
        await $('#add-weapon-form #weapon_range').val("N/A");
        await $('#add-weapon-form #weight').val(0);
        await $('#add-weapon-form #damage_type').val("N/A");
        await $('#add-weapon-form #weapon_type').val("Magic");
        await $('#add-weapon-form #rarity').val("Rare");
        await $('#add-weapon-form #condition').val("Good");
        await $('#add-weapon-form #damage').val("N/A");
        await $('#add-weapon-form #description').val(res.desc);
    }
});


$(".armor-drop").on("click", async function(event) {
    event.preventDefault();
    $targ = $(event.target);

    resp = await axios.get(`https://www.dnd5eapi.co${$targ.attr("data-url")}`);

    res = resp.data;

    await $('#add-item-form #name').val(res.name);

    if (res.armor_category) {
        let str = "";
        for (let val in res.armor_class){
            str += val;
            str += ":";
            str += " "
            str += res.armor_class[val]
            str += ","
            str += " "    
        }
        await $('#add-item-form #armor_class').val(str);
        await $('#add-item-form #weight').val(res.weight);
        await $('#add-item-form #quantity').val("1");
        await $('#add-item-form #rarity').val("N/A");
        await $('#add-item-form #condition').val("Good");
        if (res.desc) {
            await $('#add-item-form #description').val(res.desc);
        }
        else {
            await $('#add-item-form #description').val('N/A');
        }
        if (resp.data.cost) {
            await $('#add-item-form #notes').val("Cost: " + res.cost.quantity + res.cost.unit);
        }  
    }
    else if (res.desc) {
        await $('#add-item-form #armor_class').val("N/A");
        await $('#add-item-form #weight').val(0);
        await $('#add-item-form #quantity').val("1");
        await $('#add-item-form #rarity').val("Rare");
        await $('#add-item-form #condition').val("Good");
        await $('#add-item-form #description').val(res.desc);
        await $('#add-item-form #notes').val("Magic Item");
    }

    $('#add-item-form #is_wearable').prop("checked", true);
})

$(".item-drop").on("click", async function(event) {
    event.preventDefault();
    $targ = $(event.target);

    resp = await axios.get(`https://www.dnd5eapi.co${$targ.attr("data-url")}`);

    let res = resp.data;

    await $('#add-item-form #name').val(res.name);
    await $('#add-item-form #armor_class').val("N/A");
    await $('#add-item-form #description').val(res.desc);
    if (res.desc) {
        await $('#add-item-form #description').val(res.desc);
    }
    if (res.weight) {
        await $('#add-item-form #weight').val(res.weight);
    }
    else {
        await $('#add-item-form #weight').val("N/A");
    }
    await $('#add-item-form #quantity').val("1");
    await $('#add-item-form #rarity').val("Rare");
    await $('#add-item-form #condition').val("Good");

    if (resp.data.cost) {
        await $('#add-item-form #notes').val("Cost: " + res.cost.quantity + res.cost.unit);
    }
});