[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "DP700D_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared DP700D = let
  Source = AzureDataExplorer.Contents("https://trd-ktvdhje3sszzwvvfg7.z7.kusto.fabric.microsoft.com"),
  #"Navigation 1" = Source{[Name = "e042ad32-b32c-4069-bee4-18929b0cfae1"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Name = "DP700D"]}[Data]
in
  #"Navigation 2";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "DP700F_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "Neighbourhood", DestinationColumnName = "Neighbourhood"], [SourceColumnName = "SUM_No_Bikes", DestinationColumnName = "SUM_No_Bikes"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared DP700F = let
  Source = AzureDataExplorer.Contents("https://trd-ktvdhje3sszzwvvfg7.z7.kusto.fabric.microsoft.com"),
  #"Navigation 1" = Source{[Name = "e042ad32-b32c-4069-bee4-18929b0cfae1"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Name = "DP700F"]}[Data],
  #"Changed column type" = Table.TransformColumnTypes(#"Navigation 2", {{"SUM_No_Bikes", type number}})
in
  #"Changed column type";
shared DP700D_DataDestination = let
  Pattern = Lakehouse.Contents([CreateNavigationProperties = false]),
  Navigation_1 = Pattern{[workspaceId = "9711613c-9339-4abf-b363-33cc11cd07cf"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "f5057eb6-6be7-4b2d-a06a-34370fe94827"]}[Data],
  TableNavigation = Navigation_2{[Id = "DP700D", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
shared DP700F_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false]),
  Navigation_1 = Pattern{[workspaceId = "17865aab-61cf-48c0-aec0-4320f4200b00"]}[Data],
  Navigation_2 = Navigation_1{[warehouseId = "3892e394-56ec-4326-b985-44b251c7df39"]}[Data],
  TableNavigation = Navigation_2{[Item = "DP700F", Schema = "dbo"]}?[Data]?
in
  TableNavigation;
