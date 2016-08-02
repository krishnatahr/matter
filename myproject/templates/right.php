<form name="qsearch" action="search_maid_result.php" method="post"> <?php
//print_r($_SESSION["search"]);
if(isset($_GET['p']))
{
  $_REQUEST=$_SESSION["search"];
}

//print_r($_REQUEST);
 ?>
<table width="94%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td align="left" class="search_box"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                        <tr>
                          <td colspan="3" class="quick_search_title">Quick Search</td>
                        </tr>
                        <tr>
                          <td colspan="3" style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                          <td width="40%" class="quick_search_txt">Bio-data created within</td>
                          <td width="4%" class="quick_search_txt">:</td>
                          <td width="56%" align="right"><select name="select2" size="1" class="quick_search_area" id="select2">
                              <option value="">No Preference</option>
                              <option value="<7Days" <?php if($_REQUEST['biodate']=="<7Days") {?> selected <?php } ?>>Less than 7 Days</option>
                              <option value="<15Days" <?php if($_REQUEST['biodate']=="<15Days") {?> selected <?php } ?>>Less than 15 Days</option>
                              <option value="<30Days" <?php if($_REQUEST['biodate']=="<30Days") {?> selected <?php } ?>>Less than 30 Days</option>
                            </select></td>
                        </tr>
                        <tr>
                          <td colspan="3" style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                          <td class="quick_search_txt">Type of Maid</td>
                          <td class="quick_search_txt">:</td>
                          <td><select name="tom" size="1" class="quick_search_area" id="select3">
                                            <option value="">No Preference</option>
                                            <?php $sqltom=DB("SELECT * FROM maid_category WHERE type='tom'");
											while($fetchtom=mysql_fetch_array($sqltom))
											{?>
                                            <option value="<?php echo $fetchtom['name'];?>" <?php if($_REQUEST['tom']==$fetchtom['name']) { echo "selected"; } ?>><?php echo $fetchtom['name'];?></option>
                                            <?php } ?>
                                        </select></td>
                        </tr>
                        <tr>
                          <td colspan="3" style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                          <td class="quick_search_txt">Language</td>
                          <td class="quick_search_txt">:</td>
                          <td><select name="language[]" size="1" class="quick_search_area" id="select2">
                                            <option value="">No Preference</option>
                                            <?php $sqllan=DB("SELECT * FROM maid_category WHERE type='lan'");
											while($fetchlan=mysql_fetch_array($sqllan))
											{?>
                                            <option value="<?php echo $fetchlan['categoryid'];?>" <?php if(implode(",",$_REQUEST['language'])==$fetchlan['categoryid']) { echo "selected"; } ?>><?php echo $fetchlan['name'];?></option>
                                            <?php } ?>
                                        </select></td>
                        </tr>
                        <tr>
                          <td colspan="3" style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                          <td class="quick_search_txt">Marital Status</td>
                          <td class="quick_search_txt">:</td>
                          <td><select name="mstatus[]" size="1" class="quick_search_area" id="select8">
                            <option value="">No Preference</option>
							<?php $sqlms=DB("SELECT * FROM maid_category WHERE type='ms'");
								while($fetchms=mysql_fetch_array($sqlms))
								{?>
								<option value="<?php echo $fetchms['name'];?>" <?php if(implode(",",$_REQUEST['mstatus'])==$fetchms['name']) { echo "selected"; } ?>><?php echo $fetchms['name'];?></option>
								<?php } ?>
                        </select></td>
                        </tr>
                        <tr>
                          <td colspan="3" style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                        <td  class="quick_search_link"><a href="search_maid.php">Advanced Search</a></td>
                        <td class="quick_search_link">&nbsp;</td>
                        <td align="center"> <a href="#" onclick="Javascript:document.qsearch.submit();"><img src="images/search.jpg" alt="" width="70" height="23" border="0" /></a></td>
                      </tr>
                      </table>
                      </form>
                      </td>
                  </tr>
                  <tr>
                    <td align="left">&nbsp;</td>
                  </tr>
                  <tr>
                      <td align="left"><img src="images/certify.jpg" alt="" width="282" /></td>
                    </tr>
                    <tr>
                      <td align="left">&nbsp;</td>
                    </tr>
                    <?php if(!isset($_SESSION['ID'])) { ?>
                  <tr>
                    <td align="left" class="login_box">
                       <?php include("right_login.php"); ?>
                    </td>
                  </tr>

                  <tr>
                    <td align="left">&nbsp;</td>
                  </tr>
                 <?php } ?>
                </table>